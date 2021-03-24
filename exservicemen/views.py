from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from django.views.generic.edit import FormView
from . import forms
from .models import *
from exservicemen.forms import ApplyForm1, CustomUserCreationForm, PersonalForm, EmploymentForm, SpouseForm, \
    DependentForm, PensionForm, ServiceForm, ContactForm1, ContactForm2, ESMBasic, ServiceDetail
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.forms import formset_factory
from django.contrib.auth.decorators import user_passes_test


def wo_check(user):
    return user.role == 2


def homeview(request):
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
                    return HttpResponseRedirect(reverse('home'))
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
                    return HttpResponseRedirect(reverse('home'))
        return HttpResponse("INVALID CREDENTIALS")

    else:
        return render(request, 'exservicemen/usertemplates/officer_login.html')


@login_required()
def userlogout(request):
    logout(request)
    return HttpResponseRedirect(reverse('home'))


def applyview(request):
    if request.user.is_authenticated:
        return HttpResponseRedirect(reverse('home'))
    else:
        if request.method == "POST":
            login_form = CustomUserCreationForm(request.POST)
            basic_form = ApplyForm1(request.POST, request.FILES)

            if basic_form.is_valid() and login_form.is_valid():
                user = login_form.save(commit=False)
                user.is_active = False
                user.role = 1
                user.save()

                basic = basic_form.save(commit=False)
                basic.ref = user
                basic.save()

            else:
                print(login_form.errors, basic_form.errors)
            return redirect('home')



        else:
            loginform = CustomUserCreationForm
            basicform = ApplyForm1
            return render(request, "exservicemen/usertemplates/apply.html",
                          {'loginform': loginform, 'basicform': basicform})


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

# def load_mcs(request):
#     user = request.user
#     service = ServiceDetail.objects.filter(ref=user).values('service')
#     mcs = MedicalCategory.objects.filter(service=service)
#     return render(request, 'exservicemen/usertemplates/dependent_dropdown.html', {'record_offices': mcs})


# @login_required()
# def serviceformview(request):
#     if request.method == "POST":
#         pension_form = PensionForm(data=request.POST)
#
#         if pension_form.is_valid():
#             form = pension_form.save(commit=False)
#             form.ref = request.user
#             form.save()
#         return redirect('employment details')
#     else:
#         form = ServiceForm
#         return render(request, 'exservicemen/usertemplates/pension_form.html', {'form': form, 'title': 'PENSION DETAILS'})

@login_required()
def pensionformview(request):
    email = request.session['email']
    if request.method == "POST":
        pension_form = PensionForm(data=request.POST)

        if pension_form.is_valid():
            user = MyUser.objects.get(email=email)
            form = pension_form.save(commit=False)
            form.ref = user
            form.save()
            return redirect('personal details')
        return redirect('pension details')
    else:
        form = PensionForm
        service_id = request.session['service_id']
        mcs = MedicalCategory.objects.filter(service_id=service_id).all()
        return render(request, 'exservicemen/usertemplates/pension_form.html', {'form': form, 'mcs': mcs})


@login_required()
def personalformview(request):
    email = request.session['email']
    if request.method == "POST":
        personal_form = PersonalForm(data=request.POST)

        if personal_form.is_valid():
            user = MyUser.objects.get(email=email)
            form = personal_form.save(commit=False)
            form.ref = user
            form.save()
            return redirect('contact details')
        else:
            print(personal_form.errors)
            return redirect('personal details')
    else:
        form = PersonalForm
        return render(request, 'exservicemen/usertemplates/personal_form.html', {'form': form, 'title': 'PERSONAL DETAILS'})


@login_required()
def employmentformview(request):
    if request.method == "POST":
        employment_form = EmploymentForm(data=request.POST)

        if employment_form.is_valid():
            form = employment_form.save(commit=False)
            form.ref = request.user
            form.save()
        return redirect('spouse details')
    else:
        form = EmploymentForm
        return render(request, 'exservicemen/usertemplates/employment_form.html', {'form': form, 'title': 'EMPLOYMENT DETAILS'})


@login_required()
def spouseformview(request):
    if request.method == "POST":
        spouse_form = SpouseForm(data=request.POST)

        if spouse_form.is_valid():
            form = spouse_form.save(commit=False)
            form.ref = request.user
            form.save()
        return redirect('dependent details')
    else:
        form = SpouseForm
        return render(request, 'exservicemen/usertemplates/spouse_form.html', {'form': form})


@login_required()
def dependentformview(request):

    dependentformset = formset_factory(DependentForm, max_num=5, min_num=0)
    if request.method == "POST":
        formset = dependentformset(data=request.POST or None)
        if formset.is_valid():
            for form in formset:
                if form.is_valid():
                    dep = form.save(commit=False)
                    dep.ref = request.user
                    form.save()
            return redirect('home')

    else:
        formset = dependentformset()
        return render(request, 'exservicemen/usertemplates/dependent_form.html', {'formset': formset})

@login_required()
def contactformview(request):
    email = request.session['email']
    if request.method == "POST":
        contactform1 = ContactForm1(data=request.POST)

        if contactform1.is_valid():
            user = MyUser.objects.get(email=email)
            form = contactform1.save(commit=False)
            form.ref = user
            form.save()
            if contactform1.cleaned_data['is_address_same'] == 'N':
                contactform2 = ContactForm2(data=request.POST)
                if contactform2.is_valid():
                    form = contactform2.save(commit=False)
                    form.ref = user
                    form.save()
                    return redirect('spouse details')
                else:
                    print(contactform2.errors)
            else:
                return redirect('spouse details')
        else:
            print(contactform1.errors)

    form1 = ContactForm1
    form2 = ContactForm2
    return render(request, 'exservicemen/usertemplates/contact_form.html', {'form1': form1, 'form2': form2})


@login_required()
@user_passes_test(wo_check)
def addesm(request):
    if request.method == "POST":
        login_form = CustomUserCreationForm(request.POST)
        esmbasic = ESMBasic(request.POST)
        serviceform = ServiceForm(request.POST)
        WO = request.user
        zid = WelfareOfficer.objects.get(ref=WO)

        if esmbasic.is_valid() and serviceform.is_valid() and login_form.is_valid():

            user = login_form.save(commit=False)
            user.is_active = True
            user.role = 1
            user.save()

            basic = esmbasic.save(commit=False)
            basic.ref = user
            basic.save()

            service = serviceform.save(commit=False)
            service.zila_board_id = zid.zila_board_id
            service.ref = user
            request.session['service_id'] = serviceform.cleaned_data["service"].id
            request.session['email'] = login_form.cleaned_data['email']
            service.save()
            return redirect('pension details')
        else:
            print(esmbasic.errors, serviceform.errors, login_form.errors)
    loginform = CustomUserCreationForm
    esmbasic  = ESMBasic
    serviceform = ServiceForm
    return render(request, "exservicemen/usertemplates/WO_registration_home.html",
                  {'loginform': loginform, 'serviceform': serviceform, 'esmbasic': esmbasic})