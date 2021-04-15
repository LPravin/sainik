from django.shortcuts import render, redirect, get_object_or_404
from django.template.loader import render_to_string
from .forms import *
from .models import *
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse, JsonResponse
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.decorators import user_passes_test


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
    email = request.session['email']
    service_id = request.session['service_id']
    user = MyUser.objects.get(email=email)
    if request.method == "POST":
        pensionform = PensionForm(request.POST)
        try:
            check = PensionDetail.objects.get(ref=user)
        except PensionDetail.DoesNotExist:
            if pensionform.is_valid():
                user = MyUser.objects.get(email=email)
                pension = pensionform.save(commit=False)
                pension.ref = user
                pension.save()
                return redirect('personal details')
        else:
            pensionform.instance = check
            if pensionform.is_valid():
                pensionform.save()
                return redirect('personal details')
        mcs = MedicalCategory.objects.filter(service_id=service_id).all()
    else:
        mcs = MedicalCategory.objects.filter(service_id=service_id).all()
        try:
            check = PensionDetail.objects.get(ref=user)
        except PensionDetail.DoesNotExist:
            pensionform = PensionForm

        else:
            pensionform = PensionForm(instance=check)
    return render(request, 'exservicemen/officertemplates/pension.html',  {'form': pensionform, 'mcs': mcs})


@login_required()
def personalformview(request):
    email = request.session['email']
    user = MyUser.objects.get(email=email)
    if request.method == "POST":
        personalform = PersonalForm(request.POST)
        try:
            check = PersonalDetail.objects.get(ref=user)
        except PersonalDetail.DoesNotExist:
            if personalform.is_valid():
                user = MyUser.objects.get(email=email)
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
        personalform = PersonalForm
        try:
            check = PersonalDetail.objects.get(ref=user)
        except PersonalDetail.DoesNotExist:
            pass
        else:
            personalform = PersonalForm(instance=check)
    return render(request, 'exservicemen/officertemplates/personal.html', {'form': personalform})


@login_required()
def employmentformview(request):
    email = request.session['email']
    user = MyUser.objects.get(email=email)
    if request.method == "POST":
        employmentform = EmploymentForm(data=request.POST)
        user = MyUser.objects.get(email=email)
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
    return render(request, 'exservicemen/officertemplates/employment.html', {'form': employmentform, 'title': 'EMPLOYMENT DETAILS'})


@login_required()
def spouseformview(request):
    email = request.session['email']
    user = MyUser.objects.get(email=email)
    if request.method == "POST":
        spouseform = SpouseForm(request.POST)
        try:
            check = SpouseDetail.objects.get(ref=user)
        except SpouseDetail.DoesNotExist:
            if spouseform.is_valid():
                form = spouseform.save(commit=False)
                user = MyUser.objects.get(email=email)
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
    return render(request, 'exservicemen/officertemplates/spouse.html', {'form': spouseform})


# @login_required()
def dependentformview(request):
    email = request.session['email']
    user = MyUser.objects.get(email=email)
    forms = DependentDetail.objects.filter(ref=user)
    context = {'forms': forms}
    return render(request, 'exservicemen/officertemplates/dependent.html', context)


@login_required()
def contactformview(request):
    email = request.session['email']
    user = MyUser.objects.get(email=email)
    if request.method == "POST":
        form1 = ContactForm1(data=request.POST)
        form2 = ContactForm2

        try:
            check = PermanentAddress.objects.get(ref=user)
        except PermanentAddress.DoesNotExist:
            if form1.is_valid():
                user = MyUser.objects.get(email=email)
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
    return render(request, 'exservicemen/officertemplates/contact.html', {'form1': form1, 'form2': form2})


@login_required()
@user_passes_test(wo_check)
def addesm(request, pk):
    esm = ExServiceMen.objects.get(pk=pk)
    unregistered = esm.ref
    request.session['email'] = unregistered.email
    try:
        check = ServiceDetail.objects.get(ref=unregistered)
    except ServiceDetail.DoesNotExist:
        return redirect("service details")
    try:
        check = PensionDetail.objects.get(ref=unregistered)
    except PensionDetail.DoesNotExist:
        request.session['service_id'] = ServiceDetail.objects.get(ref=unregistered).service_id
        return redirect("pension details")
    try:
        check = PersonalDetail.objects.get(ref=unregistered)
    except PersonalDetail.DoesNotExist:
        return redirect("personal details")
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
    pendings = ExServiceMen.objects.filter(status=4, zila_board=zboard)[:3]
    if request.method == "POST":
        loginform = CustomUserCreationForm(request.POST)
        esmbasic = ESMBasic(request.POST)
        if loginform.is_valid() and esmbasic.is_valid():
            user = loginform.save(commit=False)
            user.is_active = True
            user.role = 1
            user.save()
            basic = esmbasic.save(commit=False)
            basic.ref = user
            basic.zila_board = zboard
            basic.status = 4
            basic.save()
            request.session['email'] = loginform.cleaned_data['email']
            regcat = esmbasic.cleaned_data['reg_category']
            request.session['reg_type'] = regcat
            if regcat != 2:
                return redirect('service details')
            else:
                return redirect('home')

    else:
        loginform = CustomUserCreationForm
        esmbasic = ESMBasic
    return render(request, "exservicemen/officertemplates/add_users_home.html",
                  {'loginform': loginform, 'esmbasic': esmbasic, 'zsbcode': zsbcode, 'rsbcode': rsbcode, 'pendings': pendings})


@login_required()
@user_passes_test(wo_check)
def serviceformview(request):
    email = request.session['email']
    user = MyUser.objects.get(email=email)
    if request.method == "POST":
        serviceform = ServiceForm(request.POST)
        try:
            check = ServiceDetail.objects.get(ref=user)
        except ServiceDetail.DoesNotExist:
            if serviceform.is_valid():
                # request.session['serviceform_data'] = serviceform.cleaned_data
                service = serviceform.save(commit=False)
                service.ref = user
                request.session['service_id'] = serviceform.cleaned_data["service"].id
                service.save()
                return redirect('pension details')
        else:
            serviceform.instance = check
            if serviceform.is_valid():
                serviceform.save()
                request.session['service_id'] = serviceform.cleaned_data["service"].id
                return redirect('pension details')
    else:
        try:
            check = ServiceDetail.objects.get(ref=user)
        except ServiceDetail.DoesNotExist:
            serviceform = ServiceForm
        else:
            serviceform = ServiceForm(instance=check)
    return render(request, "exservicemen/officertemplates/service.html",
                  {'serviceform': serviceform})


def load_record_office(request):
    service_id = request.GET.get('service_id')
    record_offices = RecordOffice.objects.filter(service_id=service_id).all()
    return render(request, 'exservicemen/usertemplates/record_office_dropdown.html', {'items': record_offices})


def load_army_records(request):
    corps_id = request.GET.get('corps_id')
    record = Corp.objects.get(id=corps_id).record_office_id
    record_office = RecordOffice.objects.filter(pk=record).all()
    return render(request, 'exservicemen/usertemplates/record_office_dropdown.html', {'items': record_office})


def load_trades(request):
    service_id = request.GET.get('service_id')
    group_id = request.GET.get('groupid')
    trades = Trade.objects.filter(service=service_id, trade_group=group_id).all()
    return render(request, 'exservicemen/usertemplates/dependent_dropdown.html', {'items': trades})


def load_ranks(request):
    service_id = request.GET.get('service_id')
    rankcatid = request.GET.get('rankcatid')
    ranks = Rank.objects.filter(service=service_id, rank_category=rankcatid).all()
    return render(request, 'exservicemen/usertemplates/dependent_dropdown.html', {'items': ranks})


def load_districts(request):
    stateid = request.GET.get('stateid')
    districts = District.objects.filter(state_id=stateid).all()
    return render(request, 'exservicemen/usertemplates/dependent_dropdown.html', {'items': districts})


def load_dependent(request):
    email = request.session['email']
    user = MyUser.objects.get(email=email)
    dependents = DependentDetail.objects.filter(ref=user)
    return render(request, 'exservicemen/officertemplates/dep_list.html', {'dependents': dependents})


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
    data['html_form'] = render_to_string('exservicemen/officertemplates/dep_update.html', context, request=request)
    return JsonResponse(data)


def add_dependent(request):
    email = request.session['email']
    user = MyUser.objects.get(email=email)
    data = dict()
    if request.method == 'POST':
        form = DependentForm(request.POST)
        if form.is_valid():
            dependent = form.save(commit=False)
            dependent.ref = user
            dependent.save()
            data['form_is_valid'] = True
            dependents = DependentDetail.objects.filter(ref=user)
            data['html_dep_list'] = render_to_string('exservicemen/officertemplates/dep_list.html', {
                'dependents': dependents
            })
        else:
            data['form_is_valid'] = False
    else:
        form = DependentForm()
    context = {'form': form}
    data['html_form'] = render_to_string('exservicemen/officertemplates/add_dep_temp.html', context, request=request)
    return JsonResponse(data)


def delete_dependent(request, pk):
    email = request.session['email']
    user = MyUser.objects.get(email=email)
    data = dict()
    dependent = get_object_or_404(DependentDetail, pk=pk)
    dependent.delete()
    dependents = DependentDetail.objects.filter(ref=user)
    data['html_dependents'] = render_to_string('exservicemen/officertemplates/dep_list.html',
                                               {'dependents': dependents})
    return JsonResponse(data)


def widowformview(request):
    email = request.session['email']
    user = MyUser.objects.get(email=email)
    if request.method == "POST":
        widowform = WidowForm(request.POST)
        if widowform.is_valid():
            form = widowform.save(commit=False)
            user = MyUser.objects.get(email=email)
            form.ref = user
            form.save()
    else:
        widowform = WidowForm
    return render(request, 'exservicemen/officertemplates/widow.html', {'form': widowform})