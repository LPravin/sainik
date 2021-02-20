from django.shortcuts import render
from django.http import HttpResponse
from . import forms
# Create your views here.


def index(request):
    return HttpResponse("<b>hi thid id bold</b>")


def login(request):
    form = forms.Login()
    return render(request, "exserivcemen/usertemplates/login.html", {'form':form})


def registration(request):
    form = forms.Registration()
    return render(request, "exserivcemen/usertemplates/registration.html", {'form': form})


def postregistration(request):
    form1 = forms.Service()
    form2 = forms.Personal()
    form3 = forms.Employment()
    form4 = forms.Spouse()
    return render(request, "exserivcemen/usertemplates/postregistration.html", {'form1': form1, 'form2': form2, 'form3': form3, 'form4': form4})