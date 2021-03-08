from django.shortcuts import render
from django.views.generic import TemplateView
from django.views.generic.edit import FormView
from . import forms
from .models import RecordOffice, Trade, Rank, District
from exservicemen.forms import ApplyForm1, CustomUserCreationForm, PersonalForm, EmploymentForm, DischargeForm, \
    SpouseForm, DependentForm
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.contrib.auth.decorators import login_required


def HomeView(request):
    return render(request, "exservicemen/usertemplates/home.html")


def userlogin(request):

    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')

        user = authenticate(email=email, password=password)

        if user:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect(reverse('home'))
            else:
                return HttpResponse("ACCOUNT IS NOT ACTIVE")
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
    if request.method == "POST":
        basic_form = ApplyForm1(data=request.POST)
        login_form = CustomUserCreationForm(data=request.POST)

        if basic_form.is_valid() and login_form.is_valid():
            user = login_form.save()
            user.set_password(user.password)
            user.save()

            basic = basic_form.save(commit=False)
            basic.ref = user
            basic.save()
        return render(request, 'exservicemen/usertemplates/home.html')
    else:
        form1 = ApplyForm1
        form2 = CustomUserCreationForm

        return render(request, "exservicemen/usertemplates/apply.html", {'form1': form1, 'form2': form2})


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
            personal = personal_form.save(commit=False)
            personal.ref = request.user
            personal.save()
        return render(request, 'exservicemen/usertemplates/home.html')
    else:
        form = PersonalForm
        return render(request, 'exservicemen/usertemplates/registration.html', {'form': form, 'title': 'PERSONAL DETAILS'})


@login_required()
def dischargeformview(request):
    if request.method == "POST":
        personal_form = PersonalForm(data=request.POST)

        if personal_form.is_valid():
            personal = personal_form.save(commit=False)
            personal.ref = request.user
            personal.save()
        return render(request, 'exservicemen/usertemplates/home.html')
    else:
        form = DischargeForm
        return render(request, 'exservicemen/usertemplates/registration.html', {'form': form, 'title': 'DISCHARGE DETAILS'})

@login_required()
def employementformview(request):
    form = EmploymentForm
    return render(request, 'exservicemen/usertemplates/registration.html', {'form': form, 'title': 'EMPLOYMENT DETAILS'})


@login_required()
def spouseformview(request):
    form = SpouseForm
    return render(request, 'exservicemen/usertemplates/registration.html', {'form': form, 'title': 'SPOUSE DETAILS'})


@login_required()
def dependentformview(request):
    form = DependentForm
    return render(request, 'exservicemen/usertemplates/registration.html', {'form': form, 'title': 'DEPENDENT DETAILS'})


