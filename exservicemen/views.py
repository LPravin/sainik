from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from django.views.generic.edit import FormView
from . import forms
from .models import *
from exservicemen.forms import ApplyForm1, CustomUserCreationForm, PersonalForm, EmploymentForm, SpouseForm, \
    DependentForm, PensionForm, Service
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.forms import formset_factory


def homeview(request):
    return render(request, "exservicemen/usertemplates/home.html")


def userlogin(request):

    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')

        user = authenticate(email=email, password=password)

        if user:
            if user.role == MyUser.EXSERVICEMEN:
                if user.is_active:
                    login(request, user)
                    return HttpResponseRedirect(reverse('home'))
                else:
                    return HttpResponseRedirect("ACCOUNT IS NOT ACTIVE")
        return HttpResponse("INVALID CREDENTIALS")

    else:
        return render(request, "exservicemen/usertemplates/user_login.html")


@login_required()
def userlogout(request):
    logout(request)
    return HttpResponseRedirect(reverse('home'))


def officerlogin(request):
    return render(request, "exservicemen/usertemplates/officer_login.html")


def applyview(request):
    if request.user.is_authenticated:
        return HttpResponseRedirect(reverse('home'))
    else:
        # if request.method == "POST":
        #     login_form = CustomUserCreationForm(data=request.POST)
        #     if login_form.is_valid():
        #         user = login_form.save()
        #         a = ApplyDetail()
        #         a.ref = user
        #         a.basic_reg_type = request.POST.get("base_reg_type")
        #         a.name = request.POST.get('name')
        #         a.mobile = request.POST.get('mobile')
        #         if ('E' or 'TE' or 'EW') in a.basic_reg_type:
        #             a.esm_reg_type = request.POST.get("esm_reg_type")
        #             a.service = request.POST.get("service")
        #             a.record_office = request.POST.get("record_office")
        #             a.service_no = request.POST("service_no")
        #             a.group = request.POST.get("group")
        #             a.trade = request.POST.get("trade")
        #             a.rank_category = request.POST.get("rank_cat")
        #             a.rank = request.POST.get("rank")
        #             a.state = request.POST.get("state")
        #             a.district = request.POST.get("district")
        #
        #             if a.esm_reg_type == "2":
        #                 a.corps = request.POST.get("corps")
        #         if a.basic_reg_type == "TE":
        #             a.zsb = request.POST.get("zsb_name")
        #         if ('W' or 'EW') in a.basic_reg_type:
        #             a.expiry_date = request.POST.get("expiry_date")
        #             if a.basic_reg_type == 'W':
        #                 a.esm_no = request.POST.get("esm_no")
        #         a.save()

        if request.method == "POST":
            login_form = CustomUserCreationForm(request.POST)
            basic_form = ApplyForm1(request.POST, request.FILES)

            print(basic_form)
            if basic_form.is_valid() and login_form.is_valid():
                user = login_form.save(commit=False)
                user.is_active = False
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


@login_required()
def personalformview(request):

    if request.method == "POST":
        personal_form = PersonalForm(data=request.POST)

        if personal_form.is_valid():
            form = personal_form.save(commit=False)
            form.ref = request.user
            form.save()
        return redirect('pension details')
    else:
        form = PersonalForm
        return render(request, 'exservicemen/usertemplates/registration.html', {'form': form, 'title': 'PERSONAL DETAILS'})


@login_required()
def pensionformview(request):
    if request.method == "POST":
        pension_form = PensionForm(data=request.POST)

        if pension_form.is_valid():
            form = pension_form.save(commit=False)
            form.ref = request.user
            form.save()
        return redirect('employment details')
    else:
        form = PensionForm
        return render(request, 'exservicemen/usertemplates/registration.html', {'form': form, 'title': 'PENSION DETAILS'})

@login_required()
def employementformview(request):
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
        return render(request, 'exservicemen/usertemplates/registration.html', {'form': form, 'title': 'SPOUSE DETAILS'})


@login_required()
def dependentformview(request):

    DependentFormset = formset_factory(DependentForm, max_num=5, min_num=0)
    if request.method == "POST":
        formset = DependentFormset(data=request.POST or None)
        if formset.is_valid():
            for form in formset:
                if form.is_valid():
                    dep = form.save(commit=False)
                    dep.ref = request.user
                    form.save()
            return redirect('home')

    else:
        formset = DependentFormset()
        return render(request, 'exservicemen/usertemplates/dependent_form.html', {'formset': formset, 'title': 'DEPENDENT DETAILS'})


