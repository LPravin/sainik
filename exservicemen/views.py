from django.shortcuts import render, redirect
# from django.views.generic import TemplateView
# from django.views.generic.edit import FormView
from .forms import *
from .models import *
# from exservicemen.forms import ApplyForm1, CustomUserCreationForm, PersonalForm, EmploymentForm, SpouseForm, \
#     DependentForm, PensionForm, ServiceForm, ContactForm1, ContactForm2, ESMBasic, ServiceDetail
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.forms import inlineformset_factory
from django.contrib.auth.decorators import user_passes_test

# FORMS = [("Service Form", ServiceForm), ("Pension Form", PensionForm), ("Personal Form", PersonalForm)]
#        # ("Spouse Form", SpouseForm), ("Dependent From", DependentForm), ("Employment Form", EmploymentForm)]
#
#
# TEMPLATES = {"Service Form": "exservicemen/officertemplates/service.html",
#              "Pension Form": "exservicemen/officertemplates/pension.html",
#              "Personal Form": "exservicemen/officertemplates/personal.html"}
#              #"Spouse Form": "exservicemen/officertemplates/spouse.html"


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
                return redirect('contact details')
        else:
            personalform.instance = check
            if personalform.is_valid():
                personalform.save()
                return redirect('contact details')
    else:
        personalform = PersonalForm
        try:
            check = PersonalDetail.objects.get(ref=user)
        except PersonalDetail.DoesNotExist:
            pass
        else:
            personalform = PersonalForm(instance=check)
    return render(request, 'exservicemen/usertemplates/personal_form.html', {'form': personalform})


@login_required()
def employmentformview(request):
    email = request.session['email']
    if request.method == "POST":
        employmentform = EmploymentForm(data=request.POST)
        user = MyUser.objects.get(email=email)
        try:
            check = EmploymentDetail.objects.get(ref=user)
        except EmploymentDetail.DoesNotExist:
            if employmentform.is_valid():
                form = employmentform.save(commit=False)
                user = MyUser.objects.get(email=email)
                form.ref = user
                form.save()
                service = ServiceDetail.objects.get(ref=user)
                service.status = 1
                return redirect('home')
        else:
            employmentform.instance = check
            if employmentform.is_valid():
                employmentform.save()
                return redirect('home')
    else:
        employmentform = EmploymentForm
    return render(request, 'exservicemen/usertemplates/employment_form.html', {'form': employmentform, 'title': 'EMPLOYMENT DETAILS'})


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
        spouseform = SpouseForm
        try:
            check = SpouseDetail.objects.get(ref=user)
        except SpouseDetail.DoesNotExist:
            pass
        else:
            spouseform.instance = check
    return render(request, 'exservicemen/officertemplates/spouse.html', {'form': spouseform})


@login_required()
def dependentformview(request):
    email = request.session['email']
    dependentformset = inlineformset_factory(MyUser, DependentDetail, DependentForm, exclude=('dep_no', 'ref',),)
    user = MyUser.objects.get(email=email)
    if request.method == "POST":
        formset = dependentformset(request.POST or None)
        dependents = DependentDetail.objects.filter(ref=user).count()
        if dependents == 0:
            if formset.is_valid():
                error = 0
                no = 1
                for form in formset:
                    if form.is_valid():
                        dep = form.save(commit=False)
                        dep.ref = user
                        dep.dep_no = no
                        dep.save()
                    else:
                        error = 1
                    no += 1
                if not error:
                    return redirect('employment details')
        else:
            if formset.is_valid():
                no = 1
                error = 0
                for form in formset:
                    try:
                        check = DependentDetail.objects.get(ref=user, dep_no=no)
                    except DependentDetail.DoesNotExist:
                        if form.is_valid(self=form):
                            dep = form.save(commit=False)
                            dep.dep_no = no
                            dep.ref = user
                            dep.save()
                        else:
                            error = 1
                    else:
                        form.instance = check
                        if form.is_valid():
                            form.save()
                        else:
                            error = 1
                if not error:
                    return redirect('employment details')
    else:
        formset = dependentformset()
        try:
            check = DependentDetail.objects.filter(ref=user).all()
        except DependentDetail.DoesNotExist:
            # no = 0
            pass
        else:
            formset = dependentformset(instance=user)
            # no = check.count()
    return render(request, 'exservicemen/officertemplates/dependent.html', {'formset': formset})


@login_required()
def contactformview(request):
    email = request.session['email']
    if request.method == "POST":
        form1 = ContactForm1(data=request.POST)
        form2 = ContactForm2
        user = MyUser.objects.get(email=email)
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
        form1 = ContactForm1
        form2 = ContactForm2
    return render(request, 'exservicemen/officertemplates/contact.html', {'form1': form1, 'form2': form2})


@login_required()
@user_passes_test(wo_check)
def addesm(request):
    # try:
    #     zid = WelfareOfficer.objects.get(ref=request.user).zila_board
    #     unregistered = ExServiceMen.objects.get(zila_board=zid, status=4)
    # except ExServiceMen.DoesNotExist:
    #     unregistered = None
    # if unregistered is None:
    return redirect('basic details')
    # else:
    #     request.session['email'] = unregistered.ref.email
    #     unregistered_user = unregistered.ref
    #     try:
    #         check = ServiceDetail.objects.get(ref=unregistered_user)
    #     except ServiceDetail.DoesNotExist:
    #         return redirect("service details")
    #     try:
    #         check = PensionDetail.objects.get(ref=unregistered_user)
    #     except PensionDetail.DoesNotExist:
    #         # request.session['service_id'] = unregistered.service_id
    #         return redirect("pension details")
    #     try:
    #         check = PersonalDetail.objects.get(ref=unregistered_user)
    #     except PersonalDetail.DoesNotExist:
    #         return redirect("personal details")
    #     try:
    #         check = SpouseDetail.objects.get(ref=unregistered_user)
    #     except SpouseDetail.DoesNotExist:
    #         return redirect("spouse details")
    #     try:
    #         check = DependentDetail.objects.get(ref=unregistered_user)
    #     except DependentDetail.DoesNotExist:
    #         return redirect('dependent details')


@login_required()
@user_passes_test(wo_check)
def addbasicinfo(request):
    if request.method == "POST":
        loginform = CustomUserCreationForm(request.POST)
        esmbasic = ESMBasic(request.POST)
        wo = request.user
        zid = WelfareOfficer.objects.get(ref=wo)
        if loginform.is_valid() and esmbasic.is_valid():
            user = loginform.save(commit=False)
            user.is_active = True
            user.role = 1
            user.save()
            basic = esmbasic.save(commit=False)
            basic.ref = user
            basic.zila_board = zid.zila_board
            basic.status = 4
            basic.save()
            request.session['email'] = loginform.cleaned_data['email']
            # request.session['esmno'] = esmbasic.cleaned_data['esm_no']
            regcat = esmbasic.cleaned_data['reg_category'].id
            request.session['reg_type'] = regcat
            if regcat != '2':
                return redirect('service details')
            else:
                return redirect('home')

    else:
        loginform = CustomUserCreationForm
        esmbasic = ESMBasic
    return render(request, "exservicemen/officertemplates/add_users_home.html",
                  {'loginform': loginform, 'esmbasic': esmbasic})


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
        serviceform = ServiceForm
        check = 0
        try:
            check = ServiceDetail.objects.get(ref=user)
        except ServiceDetail.DoesNotExist:
            pass
        serviceform.instance = check
    return render(request, "exservicemen/officertemplates/service.html",
                  {'serviceform': serviceform})


def load_record_office(request):
    service_id = request.GET.get('service_id')
    record_offices = RecordOffice.objects.filter(service_id=service_id).all()
    return render(request, 'exservicemen/usertemplates/dependent_dropdown.html', {'record_offices': record_offices})


def load_trades(request):
    service_id = request.GET.get('service_id')
    group_id = request.GET.get('groupid')
    trades = Trade.objects.filter(service=service_id, trade_group=group_id).all()
    return render(request, 'exservicemen/usertemplates/dependent_dropdown.html', {'record_offices': trades})


def load_ranks(request):
    service_id = request.GET.get('service_id')
    rankcatid = request.GET.get('rankcatid')
    ranks = Rank.objects.filter(service=service_id, rank_category=rankcatid).all()
    return render(request, 'exservicemen/usertemplates/dependent_dropdown.html', {'record_offices': ranks})


def load_districts(request):
    stateid = request.GET.get('stateid')
    districts = District.objects.filter(state_id=stateid).all()
    return render(request, 'exservicemen/usertemplates/dependent_dropdown.html', {'record_offices': districts})
