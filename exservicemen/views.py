from django.shortcuts import render, redirect, get_object_or_404
from django.template.loader import render_to_string
from .forms import *
from .models import *
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse, JsonResponse
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.decorators import user_passes_test
import datetime


def wo_check(user):
    return user.role == 2


def homeview(request):
    if request.user.is_authenticated:
        user = request.user
        if user.role == 2:
            profile = WelfareOfficer.objects.get(ref=user)
            zboard = profile.zila_board
            name = profile.name
            total_users = ExServiceMen.objects.filter(zila_board=zboard.id, status=1).count()
            return render(request, "exservicemen/usertemplates/home.html", {'zboard': zboard, 'name': name,
                                                                            'total_users':total_users})
        if user.role == 1:
            profile = ServiceDetail.objects.get(ref=user)
            name = profile.name
            return render(request, "exservicemen/usertemplates/home.html", {'name': name})

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


# @login_required()
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


@login_required()
@user_passes_test(wo_check)
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
                return redirect('home')

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
    return render(request, "exservicemen/UserForms/service.html",{'serviceform': serviceform})


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


def widowformview(request):
    esm_no = request.session['esm_no']
    user = ExServiceMen.objects.get(esm_no=esm_no)
    if request.method == "POST":
        widowform = WidowForm(request.POST)
        if widowform.is_valid():
            form = widowform.save(commit=False)
            form.ref = user
            form.save()
    else:
        widowform = WidowForm
    return render(request, 'exservicemen/UserForms/widow.html', {'form': widowform})