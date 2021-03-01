from django.shortcuts import render
from django.views.generic import TemplateView
from django.views.generic.edit import FormView
from .forms import *

# Create your views here.


class HomeView(TemplateView):
    template_name = "exservicemen/usertemplates/home.html"


class LoginView(TemplateView):
    template_name = "exservicemen/usertemplates/login.html"


class ApplyView(FormView):
    form_class = ApplyForm
    template_name = "exservicemen/usertemplates/apply.html"
    #successurl


class RegistrationFormView(FormView):
    form_class = ServiceForm
    extra_context = {'title': 'SERVICE DETAILS'}
    template_name = "exservicemen/usertemplates/registration.html"


class PersonalFormView(FormView):
    form_class = PersonalForm
    extra_context = {'title': 'PERSONAL DETAILS'}
    template_name = "exservicemen/usertemplates/registration.html"


class EmploymentFormView(FormView):
    form_class = EmploymentForm
    extra_context = {'title': 'EMPLOYMENT DETAILS'}
    template_name = "exservicemen/usertemplates/registration.html"


class SpouseFormView(FormView):
    form_class = SpouseForm
    extra_context = {'title': 'SPOUSE DETAILS'}
    template_name = "exservicemen/usertemplates/registration.html"


class DependentFormView(FormView):
    form_class = DependentForm
    extra_context = {'title': 'DEPENDENT DETAILS'}
    template_name = "exservicemen/usertemplates/registration.html"


