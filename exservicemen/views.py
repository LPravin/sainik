import datetime
from django.shortcuts import render, redirect, get_object_or_404
from django.template.loader import render_to_string
from django.views.generic import ListView
from .forms import *
from .models import *
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse, JsonResponse
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.decorators import user_passes_test
import xlwt
from django.utils.dateparse import parse_date


def wo_check(user):
    return user.role == 2


def homeview(request):
    if request.user.is_authenticated:
        user = request.user
        if user.role == 2:
            profile = WelfareOfficer.objects.get(ref=user)
            zboard = profile.zila_board
            request.session['zboard'] = zboard.id
            name = profile.name
            total_users = ExServiceMen.objects.filter(zila_board=zboard.id, status=1).count()
            return render(request, "exservicemen/usertemplates/home.html", {'zboard': zboard, 'name': name,
                                                                            'total_users':total_users})
        if user.role == 1:
            name = user.email

            return redirect('service details')
    return render(request, "exservicemen/usertemplates/home.html")


def userlogin(request):

    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')

        user = authenticate(email=email, password=password)

        if user:
            if user.role == 1:
                if user.is_active:
                    login(request, user)
                    return redirect('home')
        return HttpResponse("INVALID CREDENTIALS")

    else:
        return render(request, "exservicemen/usertemplates/user_login.html")


def officerlogin(request):

    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')

        user = authenticate(email=email, password=password)
        if user:
            if user.role == 2:
                if user.is_active:
                    login(request, user)
                    return redirect('home')
        return HttpResponse("INVALID CREDENTIALS")
    else:
        return render(request, 'exservicemen/usertemplates/officer_login.html')


@login_required()
def userlogout(request):
    logout(request)
    return HttpResponseRedirect(reverse('home'))

@login_required()
def crud(request):
    return render(request, 'exservicemen/officertemplates/crud.html')


@login_required()
def pensionformview(request):
    esm_no = request.session['esm_no']
    user = ExServiceMen.objects.get(esm_no=esm_no)
    service = ServiceDetail.objects.get(ref=user).service
    enrol_date = ServiceDetail.objects.get(ref=user).enrollment_date
    reg_date = ServiceDetail.objects.get(ref=user).reg_date
    if request.method == "POST":
        pensionform = PensionForm(request.POST)
        try:
            check = PensionDetail.objects.get(ref=user)
        except PensionDetail.DoesNotExist:
            if pensionform.is_valid():
                pension = pensionform.save(commit=False)
                pension.ref = user
                pension.save()
                return redirect('personal details')
        else:
            pensionform.instance = check
            if pensionform.is_valid():
                pensionform.save()
                return redirect('personal details')
    else:
        try:
            check = PensionDetail.objects.get(ref=user)
        except PensionDetail.DoesNotExist:
            pensionform = PensionForm()
            pensionform.fields['medical_category'].queryset = MedicalCategory.objects.filter(service=service)
            pensionform.fields['discharge_date'].widget = forms.DateInput(
                attrs={'type': 'date', 'min': str(enrol_date), 'max': str(reg_date)})
        else:
            pensionform = PensionForm(instance=check)
    return render(request, 'exservicemen/UserForms/pension.html',  {'form': pensionform})


@login_required()
def personalformview(request):
    esm_no = request.session['esm_no']
    user = ExServiceMen.objects.get(esm_no=esm_no)
    if request.method == "POST":
        personalform = PersonalForm(request.POST)
        try:
            check = PersonalDetail.objects.get(ref=user)
        except PersonalDetail.DoesNotExist:
            if personalform.is_valid():
                form = personalform.save(commit=False)
                form.ref = user
                form.save()
                return redirect('employment details')
        else:
            personalform.instance = check
            if personalform.is_valid():
                personalform.save()
                return redirect('employment details')
    else:
        try:
            check = PersonalDetail.objects.get(ref=user)
        except PersonalDetail.DoesNotExist:
            personalform = PersonalForm()
        else:
            personalform = PersonalForm(instance=check)
    return render(request, 'exservicemen/UserForms/personal.html', {'form': personalform})


@login_required()
def employmentformview(request):
    esm_no = request.session['esm_no']
    user = ExServiceMen.objects.get(esm_no=esm_no)
    if request.method == "POST":
        employmentform = EmploymentForm(data=request.POST)
        try:
            check = EmploymentDetail.objects.get(ref=user)
        except EmploymentDetail.DoesNotExist:
            if employmentform.is_valid():
                form = employmentform.save(commit=False)
                form.ref = user
                form.save()
                service = ServiceDetail.objects.get(ref=user)
                service.status = 1
                return redirect('contact details')
        else:
            employmentform.instance = check
            if employmentform.is_valid():
                employmentform.save()
                return redirect('contact details')
    else:
        employmentform = EmploymentForm
        try:
            check = EmploymentDetail.objects.get(ref=user)
        except EmploymentDetail.DoesNotExist:
            pass
        else:
            employmentform = EmploymentForm(instance=check)
    return render(request, 'exservicemen/UserForms/employment.html', {'form': employmentform, 'title': 'EMPLOYMENT DETAILS'})


@login_required()
def spouseformview(request):
    esm_no = request.session['esm_no']
    user = ExServiceMen.objects.get(esm_no=esm_no)
    if request.method == "POST":
        spouseform = SpouseForm(request.POST)
        try:
            check = SpouseDetail.objects.get(ref=user)
        except SpouseDetail.DoesNotExist:
            if spouseform.is_valid():
                form = spouseform.save(commit=False)
                form.ref = user
                form.save()
                return redirect('dependent details')
        else:
            spouseform.instance = check
            if spouseform.is_valid():
                spouseform.save()
                return redirect('dependent details')
    else:
        try:
            check = SpouseDetail.objects.get(ref=user)
        except SpouseDetail.DoesNotExist:
            spouseform = SpouseForm
        else:
            spouseform = SpouseForm(instance=check)
    return render(request, 'exservicemen/UserForms/spouse.html', {'form': spouseform})


@login_required()
def dependentformview(request):
    esm_no = request.session['esm_no']
    user = ExServiceMen.objects.get(esm_no=esm_no)
    forms = DependentDetail.objects.filter(ref=user)
    context = {'forms': forms}
    return render(request, 'exservicemen/UserForms/dependent.html', context)


def submit(request):
    esm_no = request.session['esm_no']
    reg_user = ExServiceMen.objects.get(esm_no=esm_no)
    reg_user.status = 1
    reg_user.save()
    return redirect('home')


@login_required()
def contactformview(request):
    esm_no = request.session['esm_no']
    user = ExServiceMen.objects.get(esm_no=esm_no)
    if request.method == "POST":
        form1 = ContactForm1(data=request.POST)
        form2 = ContactForm2

        try:
            check = PermanentAddress.objects.get(ref=user)
        except PermanentAddress.DoesNotExist:
            if form1.is_valid():
                form = form1.save(commit=False)
                form.ref = user
                form.save()
                if form1.cleaned_data['is_address_same'] == 0:
                    form2 = ContactForm2(data=request.POST)
                    if form2.is_valid():
                        form = form2.save(commit=False)
                        form.ref = user
                        form.save()
                        return redirect('spouse details')
                else:
                    return redirect('spouse details')
        else:
            form1.instance = check
            if form1.is_valid():
                form1.save()
                if form1.cleaned_data['is_address_same'] == 0:
                    form2 = ContactForm2(request.POST)
                    try:
                        check1 = PresentAddress.objects.get(ref=user)
                    except PresentAddress.DoesNotExist:
                        if form2.is_valid():
                            form = form2.save(commit=False)
                            form.ref = user
                            form.save()
                            return redirect('spouse details')
                    else:
                        form2.instance = check1
                        if form2.is_valid():
                            form2.save()
                            return redirect('spouse details')
                else:
                    return redirect('spouse details')
    else:
        try:
            check = PermanentAddress.objects.get(ref=user)
        except PermanentAddress.DoesNotExist:
            form1 = ContactForm1
            form2 = ContactForm2
        else:
            form1 = ContactForm1(instance=check)
            check2 = PermanentAddress.objects.get(ref=user).is_address_same
            if not check2:
                check3 = PresentAddress.objects.get(ref=user)
                form2 = ContactForm2(instance=check3)
            else:
                form2 = ContactForm2
    return render(request, 'exservicemen/UserForms/contact.html', {'form1': form1, 'form2': form2})


def documentformview(request):
    esm_no = request.session['esm_no']
    user = ExServiceMen.objects.get(esm_no=esm_no)
    if request.method == "POST":
        esmdocform = ESMDocumentForm
        spousedocform = SpouseDocumentForm
        dependentdocform = DependentDocumentForm
    else:
        esmdocform = ESMDocumentForm
        spousedocform = SpouseDocumentForm
        dependentdocform = DependentDocumentForm
    return render(request, 'exservicemen/UserForms/documents_upload.html', {'edoc': esmdocform,
                                                        'sdoc': spousedocform, 'ddoc': dependentdocform})

@login_required()
def addesm(request, pk):
    unregistered = ExServiceMen.objects.get(pk=pk)
    request.session['esm_no'] = unregistered.esm_no
    try:
        check = ServiceDetail.objects.get(ref=unregistered)
    except ServiceDetail.DoesNotExist:
        return redirect("service details")
    try:
        check = PensionDetail.objects.get(ref=unregistered)
    except PensionDetail.DoesNotExist:
        return redirect("pension details")
    try:
        check = PersonalDetail.objects.get(ref=unregistered)
    except PersonalDetail.DoesNotExist:
        return redirect("personal details")
    try:
        check = PermanentAddress.objects.get(ref=unregistered)
    except PermanentAddress.DoesNotExist:
        return redirect("contact details")
    try:
        check = EmploymentDetail.objects.get(ref=unregistered)
    except EmploymentDetail.DoesNotExist:
        return redirect("employment details")
    try:
        check = SpouseDetail.objects.get(ref=unregistered)
    except SpouseDetail.DoesNotExist:
        return redirect("spouse details")
    else:
        return redirect('dependent details')


@login_required()
@user_passes_test(wo_check)
def addbasicinfo(request):
    wo = request.user
    zboard = WelfareOfficer.objects.get(ref=wo).zila_board
    zsbcode = zboard.code
    state = zboard.state
    rsbcode = RajyaSainikBoard.objects.get(state=state).code
    pendings = ExServiceMen.objects.filter(status=4, zila_board=zboard)
    if request.method == "POST":
        esmbasic = ESMBasic(request.POST)
        if esmbasic.is_valid():
            basic = esmbasic.save(commit=False)
            basic.zila_board = zboard
            basic.status = 4
            basic.save()
            request.session['esm_no'] = esmbasic.cleaned_data['esm_no']
            regcat = esmbasic.cleaned_data['reg_category']
            request.session['reg_type'] = regcat
            if regcat != 2:
                return redirect('service details')
            else:
                return redirect('widow details')

    else:
        esmbasic = ESMBasic
    return render(request, "exservicemen/UserForms/add_users_home.html",
                  {'esmbasic': esmbasic, 'zsbcode': zsbcode, 'rsbcode': rsbcode, 'pendings': pendings})


@login_required()
@user_passes_test(wo_check)
def serviceformview(request):
    esm_no = request.session['esm_no']
    user = ExServiceMen.objects.get(esm_no=esm_no)
    if request.method == "POST":
        serviceform = ServiceForm(request.POST)
        try:
            check = ServiceDetail.objects.get(ref=user)
        except ServiceDetail.DoesNotExist:
            if serviceform.is_valid():
                service = serviceform.save(commit=False)
                service.ref = user
                service.save()
                return redirect('pension details')
        else:
            serviceform.instance = check
            if serviceform.is_valid():
                serviceform.save()
                return redirect('pension details')
    else:
        try:
            check = ServiceDetail.objects.get(ref=user)
        except ServiceDetail.DoesNotExist:
            serviceform = ServiceForm()
        else:
            serviceform = ServiceForm(instance=check)
    return render(request, "exservicemen/UserForms/service.html", {'serviceform': serviceform})


def load_record_office(request):
    service_id = request.GET.get('service_id')
    record_offices = RecordOffice.objects.filter(service_id=service_id).all()
    return render(request, 'exservicemen/UserForms/record_office_dropdown.html', {'items': record_offices})


def load_army_records(request):
    corps_id = request.GET.get('corps_id')
    record = Corp.objects.get(id=corps_id).record_office_id
    record_office = RecordOffice.objects.filter(pk=record).all()
    return render(request, 'exservicemen/UserForms/record_office_dropdown.html', {'items': record_office})


def load_trades(request):
    service_id = request.GET.get('service_id')
    group_id = request.GET.get('groupid')
    trades = Trade.objects.filter(service=service_id, trade_group=group_id).all()
    return render(request, 'exservicemen/UserForms/dependent_dropdown.html', {'items': trades})


def load_ranks(request):
    service_id = request.GET.get('service_id')
    rankcatid = request.GET.get('rankcatid')
    ranks = Rank.objects.filter(service=service_id, rank_category=rankcatid).all()
    return render(request, 'exservicemen/UserForms/dependent_dropdown.html', {'items': ranks})


def load_prefixes(request):
    service_id = request.GET.get('service_id')
    rankcat_id = request.GET.get('rankcat_id')
    prefixes = ServiceNoPrefix.objects.filter(service_id=service_id, rank_category_id=rankcat_id).all()
    return render(request, 'exservicemen/UserForms/dependent_dropdown.html', {'items': prefixes})


def load_districts(request):
    stateid = request.GET.get('stateid')
    districts = District.objects.filter(state_id=stateid).all()
    return render(request, 'exservicemen/UserForms/dependent_dropdown.html', {'items': districts})


def load_dependent(request):
    esm_no = request.session['esm_no']
    user = ExServiceMen.objects.get(esm_no=esm_no)
    dependents = DependentDetail.objects.filter(ref=user)
    return render(request, 'exservicemen/UserForms/dep_list.html', {'dependents': dependents})


def update_dependent(request, pk):
    dependent = get_object_or_404(DependentDetail, pk=pk)
    data = dict()
    if request.method == "POST":
        form = DependentForm(request.POST, instance=dependent)
        if form.is_valid():
            form.save()
            data['form_is_valid'] = True
    else:
        form = DependentForm(instance=dependent)
    context = {'form': form}
    data['html_form'] = render_to_string('exservicemen/UserForms/dep_update.html', context, request=request)
    return JsonResponse(data)


def add_dependent(request):
    esm_no = request.session['esm_no']
    user = ExServiceMen.objects.get(esm_no=esm_no)
    data = dict()
    if request.method == 'POST':
        form = DependentForm(request.POST)
        if form.is_valid():
            dependent = form.save(commit=False)
            dependent.ref = user
            dependent.save()
            data['form_is_valid'] = True
            dependents = DependentDetail.objects.filter(ref=user)
            data['html_dep_list'] = render_to_string('exservicemen/UserForms/dep_list.html', {
                'dependents': dependents
            })
        else:
            print(form.errors)
            data['form_is_valid'] = False

    else:
        form = DependentForm()
    context = {'form': form}
    data['html_form'] = render_to_string('exservicemen/UserForms/add_dep_temp.html', context, request=request)
    return JsonResponse(data)


def delete_dependent(request, pk):
    esm_no = request.session['esm_no']
    user = ExServiceMen.objects.get(esm_no=esm_no)
    data = dict()
    dependent = get_object_or_404(DependentDetail, pk=pk)
    dependent.delete()
    dependents = DependentDetail.objects.filter(ref=user)
    data['html_dependents'] = render_to_string('exservicemen/UserForms/dep_list.html',
                                               {'dependents': dependents})
    return JsonResponse(data)


def filter_esm_list(request):
    zboard = request.session['zboard']
    # esm_list = ServiceDetail.objects.select_related('servicedetail__').filter(ref__zila_board_id=zboard).all()
    # eee = ServiceDetail.objects.select_related()
    esm_list = ExServiceMen.objects.select_related('servicedetail').only('servicedetail__name')
    # esm_list.select_related('servicedetail')
    return render(request, 'exservicemen/officertemplates/filter_esm_list.html', {'esm_list': esm_list})


def load_esm_list(request):
    zboard = request.session['zboard']
    # esm_list = ServiceDetail.objects.select_related('servicedetail__').filter(ref__zila_board_id=zboard).all()
    # eee = ServiceDetail.objects.select_related()
    esm_list = ExServiceMen.objects.select_related('servicedetail').values('esm_no',
                                                   'servicedetail__name', 'servicedetail__service_no')[:5]
    # esm_list.select_related('servicedetail')
    return render(request, 'exservicemen/UserForms/esm_list.html', {'esm_list': esm_list})


def update_esm(request, pk):
    user = ExServiceMen.objects.get(esm_no=pk)
    request.session['esm_no'] = user.esm_no
    return redirect('service details')


def search_esm(request):
    search_id = request.GET.get('sb')
    search_input = request.GET.get('search_input')
    if search_id == "1":
        esm_list = ExServiceMen.objects.filter(esm_no= search_input).select_related('servicedetail').values('esm_no',
                                      'servicedetail__name','servicedetail__service_no')
    else:
        esm_list = ExServiceMen.objects.filter(servicedetail__name=search_input).select_related('servicedetail').\
                   values('esm_no', 'servicedetail__name','servicedetail__service_no')
    return render(request, 'exservicemen/UserForms/esm_list.html', {'esm_list': esm_list})


def widowformview(request):
    esm_no = request.session['esm_no']
    user = ExServiceMen.objects.get(esm_no=esm_no)
    wo = request.user
    zboard = WelfareOfficer.objects.get(ref=wo).zila_board
    zsbcode = zboard.code
    state = zboard.state
    rsbcode = RajyaSainikBoard.objects.get(state=state).code
    if request.method == "POST":
        widowform = WidowForm(request.POST)
        if widowform.is_valid():
            form = widowform.save(commit=False)
            form.ref = user
            form.save()
    else:
        widowform = WidowForm
    return render(request, 'exservicemen/UserForms/widow.html', {'form': widowform, 'zsbcode':zsbcode, 'rsbcode': rsbcode})


def get_spouse_info(request):
    s_esm_no = request.GET.get('s_esm_no')
    try:
        esm = ExServiceMen.objects.get(esm_no=s_esm_no)
    except ExServiceMen.DoesNotExist:
        esm = None
    return render(request, 'exservicemen/UserForms/get_spouse_info.html', {'esm': esm})


def filter_result(name, rt, rc, ro, service, trade, cq, es, et, er, sj, ms, ac, dd, ed, edc, dod, dc, city, dis, st):
    a = ExServiceMen.objects.all()
    if name:
        a = a.filter(servicedetail__name__icontains=name)
    if rt:
        a = a.filter(reg_category=rt)
    if rc:
        a = a.filter(servicedetail__rank_category=rc)
    if ro:
        a = a.filter(servicedetail__record_office_id=ro)
    if sj:
        a = a.filter(employmentdetail__security_job=sj)
    if service:
        a = a.filter(servicedetail__service_id=service)
    if trade:
        a = a.filter(servicedetail__trade_id=trade)
    if cq:
        a = a.filter(employmentdetail__civil_qualification_id=cq)
    if es:
        a = a.filter(employmentdetail__employment_status__exact=es)
    if et:
        a = a.filter(servicedetail__reg_type__esm_type=et)
    if er:
        a = a.filter(employmentdetail__willing_for_job=er)
    if ms:
        a = a.filter(spousedetail__marital_status=ms)
    if ac:
        dd = parse_date(dd)
        t = datetime.date(dd.year - int(ac), dd.month, dd.day)
        a = a.filter(servicedetail__dob__lte=t)
    if edc:
        ed = parse_date(ed)
        if edc == '1':
            a = a.filter(servicedetail__enrollment_date=ed)
        elif edc == '2':
            a = a.filter(servicedetail__enrollment_date__gt=ed)
        elif edc == '3':
            a = a.filter(servicedetail__enrollment_date__lt=ed)
        elif edc == '4':
            a = a.filter(servicedetail__enrollment_date__gte=ed)
        elif edc == '5':
            a = a.filter(servicedetail__enrollment_date__lte=ed)
    if dc:
        dod = parse_date(dod)
        if dc == '1':
            a = a.filter(pensiondetail__discharge_date__exact=dod)
        elif dc == '2':
            a = a.filter(pensiondetail__discharge_date__gt=dod)
        elif dc == '3':
            a = a.filter(pensiondetail__discharge_date__lt=dod)
        elif dc == '4':
            a = a.filter(pensiondetail__discharge_date__gte=dod)
        elif dc == '5':
            a = a.filter(pensiondetail__discharge_date__lte=dod)
    if city:
        a = a.filter(permanentaddress__city=city)
    if dis:
        a = a.filter(permanentaddress__district=dis)
    if st:
        a = a.filter(permanentaddress__state=st)
    return a


def filter(request):
    if request.method == "POST":
        name = request.POST.get('name_contains')
        rt = request.POST.get('registration_types')
        rc = request.POST.get('rank_categories')
        ro = request.POST.get('record_offices')
        service = request.POST.get('services')
        trade = request.POST.get('trades')
        cq = request.POST.get('civil_qualifications')
        es = request.POST.get('employment_status')
        et = request.POST.get('esm_type')
        er = request.POST.get('employment_registration')
        sj = request.POST.get('security_job')
        ms = request.POST.get('martial_status')
        ac = request.POST.get('age_completed')
        dd = request.POST.get('dob_date')
        ed = request.POST.get('enrollment_date')
        edc = request.POST.get('ed_conditions')
        dod = request.POST.get('date_of_discharge')
        dc = request.POST.get('dod_conditions')
        city = request.POST.get('city')
        dis = request.POST.get('district')
        st = request.POST.get('state')
        a = filter_result(name, rt, rc, ro, service, trade, cq, es, et, er, sj, ms, ac, dd, ed, edc, dod, dc, city, dis,
                          st)
        response = HttpResponse(content_type='application/ms-excel')
        response['Content-Disposition'] = 'attachment; filename="users.xls"'
        wb = xlwt.Workbook(encoding='utf-8')
        ws = wb.add_sheet('Service Detail')
        row_num = 0
        font_style = xlwt.XFStyle()
        font_style.font.bold = True
        columns = ['ESM NO', 'Name', 'Service No', 'Date of Birth', 'Mobile', 'ESM Type', 'Service', 'Corps', 'Record office',
                   'Group', 'Trade', 'Rank Category', 'Rank', 'Registration Date', 'Enrollment Date']
        for col_num in range(len(columns)):
            ws.write(row_num, col_num, columns[col_num], font_style)
        font_style = xlwt.XFStyle()
        rows = a.values_list('esm_no', 'servicedetail__name', 'servicedetail__service_no', 'servicedetail__dob',
                             'servicedetail__mobile', 'servicedetail__reg_type__esm_type',
                             'servicedetail__service__service_name', 'servicedetail__corps__corps_name',
                             'servicedetail__record_office__record_office_name', 'servicedetail__group__trade_group',
                             'servicedetail__trade__trade_name', 'servicedetail__rank_category__rank_category',
                             'servicedetail__rank__rank', 'servicedetail__reg_date', 'servicedetail__enrollment_date')
        for row in rows:
            row_num += 1
            for col_num in range(len(row)):
                ws.write(row_num, col_num, row[col_num], font_style)
        wp = wb.add_sheet('Pension Detail')
        row_num = 0
        font_style = xlwt.XFStyle()
        font_style.font.bold = True
        columns = ['ESM NO', 'Name', 'Service No', 'Unit last served', 'Discharge Date', 'Discharge_reason',
                   'Medical Category', 'Character', 'Dishcarge Book No', 'PPO No', 'Pension Status', 'Pension Sanctioned',
                   'Present pension', 'Whether PWD', 'Disability Pension', 'Disability percent', 'Family Pension']
        for col_num in range(len(columns)):
            wp.write(row_num, col_num, columns[col_num], font_style)
        font_style = xlwt.XFStyle()
        rows = a.values_list('esm_no', 'servicedetail__name', 'servicedetail__service_no',
                             'pensiondetail__unit_last_served', 'pensiondetail__discharge_date',
                             'pensiondetail__discharge_reason__reason', 'pensiondetail__medical_category__mc_name',
                             'pensiondetail__character__character', 'pensiondetail__discharge_book_no',
                             'pensiondetail__ppo_no','pensiondetail__pensioner_status',
                             'pensiondetail__pension_sanctioned', 'pensiondetail__present_pension',
                             'pensiondetail__whether_pwd', 'pensiondetail__disability_pension',
                             'pensiondetail__disability_percent', 'pensiondetail__family_pension')
        for row in rows:
            row_num += 1
            for col_num in range(len(row)):
                wp.write(row_num, col_num, row[col_num], font_style)
        wa = wb.add_sheet('Personal Detail')
        row_num = 0
        font_style = xlwt.XFStyle()
        font_style.font.bold = True
        columns = ['ESM NO', 'Name', 'Service No', 'Gender', 'Mother', 'Father',
                   'Religion', 'Caste category', 'Birth Place', 'Birth District', 'Birth State',
                   'Expiry Date', 'Aadhaar No', 'Voter ID No', 'PAN No', 'CSD No', 'ECHS No', 'Identification Mark 1', 'Identification Mark 2']
        for col_num in range(len(columns)):
            wa.write(row_num, col_num, columns[col_num], font_style)
        font_style = xlwt.XFStyle()
        rows = a.values_list('esm_no', 'servicedetail__name', 'servicedetail__service_no',
                             'personaldetail__gender',
                             'personaldetail__mother', 'personaldetail__father',
                             'personaldetail__religion__religion_name',
                             'personaldetail__caste_category__caste_category_name', 'personaldetail__birth_place',
                             'personaldetail__birth_district__district_name', 'personaldetail__birth_state__state_name',
                             'personaldetail__expiry_date',
                             'personaldetail__aadhaar_no', 'personaldetail__voter_id_no',
                             'personaldetail__pan_no',
                             'personaldetail__csd_no', 'personaldetail__echs_no', 'personaldetail__ident_mark_1',
                             'personaldetail__ident_mark_2')
        for row in rows:
            row_num += 1
            for col_num in range(len(row)):
                wa.write(row_num, col_num, row[col_num], font_style)
        wc = wb.add_sheet('Permanent Address')
        row_num = 0
        font_style = xlwt.XFStyle()
        font_style.font.bold = True
        columns = ['ESM NO', 'Name', 'Service No', 'House No', 'House Name', 'Street Name',
                   'City', 'District', 'State', 'Pincode', 'Telephone', 'Is present address same']
        for col_num in range(len(columns)):
            wc.write(row_num, col_num, columns[col_num], font_style)
        font_style = xlwt.XFStyle()
        rows = a.values_list('esm_no', 'servicedetail__name', 'servicedetail__service_no',
                             'permanentaddress__house_no',
                             'permanentaddress__house_name', 'permanentaddress__street_name',
                             'permanentaddress__city',
                             'permanentaddress__district__district_name', 'permanentaddress__state__state_name',
                             'permanentaddress__pincode', 'permanentaddress__telephone',
                             'permanentaddress__is_address_same',)
        for row in rows:
            row_num += 1
            for col_num in range(len(row)):
                wc.write(row_num, col_num, row[col_num], font_style)
        wd = wb.add_sheet('Employment Details')
        row_num = 0
        font_style = xlwt.XFStyle()
        font_style.font.bold = True
        columns = ['ESM NO', 'Name', 'Service No', 'Civil qualification', 'Specialization', 'Test passed',
                   'Employment Status', 'Registered for Employment', 'Willing for security job', 'Sector', 'Monthly income',
                   'Department', "Civil retirement date", 'Civil ppo no']
        for col_num in range(len(columns)):
            wd.write(row_num, col_num, columns[col_num], font_style)
        font_style = xlwt.XFStyle()
        rows = a.values_list('esm_no', 'servicedetail__name', 'servicedetail__service_no',
                             'employmentdetail__civil_qualification__qualification',
                             'employmentdetail__specialization__specialization', 'employmentdetail__test_passed',
                             'employmentdetail__employment_status',
                             'employmentdetail__willing_for_job', 'employmentdetail__security_job','employmentdetail__sector',
                             'employmentdetail__monthly_income', 'employmentdetail__department__dep_name',
                             'employmentdetail__civil_retirement_date', 'employmentdetail__civil_ppo_no')
        for row in rows:
            row_num += 1
            for col_num in range(len(row)):
                wd.write(row_num, col_num, row[col_num], font_style)
        we = wb.add_sheet('Spouse Details')
        row_num = 0
        font_style = xlwt.XFStyle()
        font_style.font.bold = True
        columns = ['ESM NO', 'Name', 'Service No', 'Marital Status', 'Spouse Name', 'Spouse DOB',
                   'Marriage Date', 'Spouse Relation', 'Spouse Qualification', 'Specialization',
                   'Spouse employment status',
                   'Spouse profession', 'Aadhaar No', 'Voter ID No', 'PAN No',
                   'CSD No', 'ECHS No', 'Identification Mark 1', 'Identification Mark 2']
        for col_num in range(len(columns)):
            we.write(row_num, col_num, columns[col_num], font_style)
        font_style = xlwt.XFStyle()
        rows = a.values_list('esm_no', 'servicedetail__name', 'servicedetail__service_no',
                             'spousedetail__marital_status',
                             'spousedetail__spouse_name', 'spousedetail__dob',
                             'spousedetail__marriage_date',
                             'spousedetail__spouse_relation', 'spousedetail__spouse_qualification__qualification',
                             'spousedetail__specialization__specialization',
                             'spousedetail__spouse_employment_status', 'spousedetail__spouse_profession',
                             'spousedetail__aadhaar_no','spousedetail__voter_id', 'spousedetail__pan_no',
                             'spousedetail__csd_no', 'spousedetail__echs_no', 'spousedetail__ident_mark_1',
                             'spousedetail__ident_mark_2')
        for row in rows:
            row_num += 1
            for col_num in range(len(row)):
                we.write(row_num, col_num, row[col_num], font_style)
        wb.save(response)
        return response

    else:
        form = FilterForm
        return render(request, 'exservicemen/officertemplates/filter_esm.html', {'form': form})


def filter_esm(request):
    wo = request.user
    zboard = WelfareOfficer.objects.get(ref=wo).zila_board
    zsbcode = zboard.code
    name = request.GET.get('name')
    rt = request.GET.get('rt')
    rc = request.GET.get('rc')
    ro = request.GET.get('ro')
    service = request.GET.get('service')
    trade = request.GET.get('trade')
    cq = request.GET.get('cq')
    es = request.GET.get('es')
    et = request.GET.get('et')
    er = request.GET.get('er')
    sj = request.GET.get('sj')
    ms = request.GET.get('ms')
    ac = request.GET.get('ac')
    dd = request.GET.get('dd')
    ed = request.GET.get('ed')
    edc = request.GET.get('edc')
    dod = request.GET.get('dod')
    dc = request.GET.get('dc')
    city = request.GET.get('city')
    dis = request.GET.get('dis')
    st = request.GET.get('st')
    a = filter_result(name, rt, rc, ro, service, trade, cq, es, et, er, sj, ms, ac, dd, ed, edc, dod, dc, city, dis, st)
    a = a.filter(zila_board=zboard)
    return render(request, 'exservicemen/officertemplates/filter_esm_list.html', {'esm_list': a})


def xlexport(request):
    name = request.GET.get('name')
    rc = request.GET.get('rc')
    rcat = request.GET.get('rcat')
    ro = request.GET.get('ro')
    sj = request.GET.get('sj')
    service = request.GET.get('service')
    trade = request.GET.get('trade')
    cq = request.GET.get('cq')
    es = request.GET.get('es')
    a = filter_result(name, rc, rcat, ro, service, trade, cq, es)
    response = HttpResponse(content_type='application/ms-excel')
    response['Content-Disposition'] = 'attachment; filename="users.xls"'
    wb = xlwt.Workbook(encoding='utf-8')
    ws = wb.add_sheet('Report')
    row_num = 0
    font_style = xlwt.XFStyle()
    font_style.font.bold = True
    columns = ['ESM NO', 'Name', 'Service No', 'Date of Birth', ]
    for col_num in range(len(columns)):
        ws.write(row_num, col_num, columns[col_num], font_style)
    font_style = xlwt.XFStyle()
    rows = a.values_list('esm_no','servicedetail__name', 'servicedetail__service_no', 'servicedetail__dob')
    for row in rows:
        row_num += 1
        for col_num in range(len(row)):
            ws.write(row_num, col_num, row[col_num], font_style)
    wb.save(response)
    return response



# def applyview(request):
#     if request.method == "POST":
#         loginform = CustomUserCreationForm(request.POST)
#         if loginform.is_valid():
#             inactive_user = send_verification_email(request, loginform)
#     else:
#         loginform = CustomUserCreationForm
#     return render(request, 'exservicemen/usertemplates/apply.html',{'loginform': loginform})

def detailview(request):
    return render(request, 'exservicemen/officertemplates/esm_info_view.html')