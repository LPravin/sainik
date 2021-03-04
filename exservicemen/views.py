from django.shortcuts import render
from django.views.generic import TemplateView
from django.views.generic.edit import FormView
from . import forms
from .models import RecordOffice,Trade
from exservicemen.forms import ApplyForm1,CustomUserCreationForm

# Create your views here.


class HomeView(TemplateView):
    template_name = "exservicemen/usertemplates/home.html"


class LoginView(TemplateView):
    template_name = "exservicemen/usertemplates/login.html"


def applyview(request):

    registered = False
    if request.method == "POST":
        basic_form = ApplyForm1(request.POST)
        login_form = CustomUserCreationForm(request.POST)

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
    return render(request, 'exservicemen/usertemplates/record_office_dropdown.html', {'record_offices': record_offices})
    # return JsonResponse(list(cities.values('id', 'name')), safe=False)

#def applysubmit(request):

    #if request.method == "POST":
def load_trades(request):
    service_id = request.GET.get('service_id')
    group_id = request.GET.get('tradegroup_id')
    trades = Trade.objects.filter(service_id=service_id, group_id=group_id).all()
    return render(request, 'exservicemen/usertemplates/record_office_dropdown.html', {'trades': trades})


class ApplyView(FormView):
    form_class = forms.ApplyForm1
    template_name = "exservicemen/usertemplates/apply.html"

class RegistrationFormView(FormView):
    form_class = forms.ServiceForm
    extra_context = {'title': 'SERVICE DETAILS'}
    template_name = "exservicemen/usertemplates/registration.html"


class PersonalFormView(FormView):
    form_class = forms.PersonalForm
    extra_context = {'title': 'PERSONAL DETAILS'}
    template_name = "exservicemen/usertemplates/registration.html"


class EmploymentFormView(FormView):
    form_class = forms.EmploymentForm
    extra_context = {'title': 'EMPLOYMENT DETAILS'}
    template_name = "exservicemen/usertemplates/registration.html"


class SpouseFormView(FormView):
    form_class = forms.SpouseForm
    extra_context = {'title': 'SPOUSE DETAILS'}
    template_name = "exservicemen/usertemplates/registration.html"


class DependentFormView(FormView):
    form_class = forms.DependentForm
    extra_context = {'title': 'DEPENDENT DETAILS'}
    template_name = "exservicemen/usertemplates/registration.html"


