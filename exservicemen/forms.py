from django import forms
from django.forms import ModelForm
from .models import *


class Login(forms.Form):
    username = forms.EmailField(label="Email")
    password = forms.CharField(widget=forms.PasswordInput())


class ApplyForm(ModelForm):
    YesNo = [
        ('Y', 'Yes'),
        ('N', 'No')
    ]
    name = forms.CharField(max_length=100)
    mail = forms.CharField(max_length=20)
    password = forms.CharField(max_length=16)
    confirm_password = forms.CharField(max_length=16)
    reg_type = forms.ChoiceField()
    have_esm = forms.ChoiceField(choices=YesNo, label="Do you have ESM Identity Card?", required=False)
    esm_no = forms.CharField(max_length=10, label="Enter ESM No:")
    expiry_date = forms.DateField()
    death_certificate = forms.ImageField()
    reg_type2 = forms.ChoiceField()
    service = forms.ChoiceField()
    corps = forms.ChoiceField()
    records = forms.ChoiceField()
    group = forms.ChoiceField()
    trade = forms.ChoiceField()
    rank_category = forms.ChoiceField()
    rank = forms.ChoiceField()
    service_no = forms.CharField(max_length=9)
    state = forms.ChoiceField()
    district = forms.ChoiceField()
    discharge_book = forms.ImageField()
    ppo_book = forms.ImageField()
    residence_certificate = forms.ImageField()

    class Meta:
        model = ServiceDetail
        fields = []
        field_order = []


class ServiceForm(ModelForm):

    class Meta:
        model = ServiceDetail
        exclude = ['zila_board_id', 'ref']
        widgets = {
            'reg_date': forms.DateInput(attrs={'type': 'date'}),
        }


class PersonalForm(ModelForm):

    class Meta:
        model = PersonalDetail
        exclude = ['ref']


class EmploymentForm(ModelForm):

    class Meta:
        model = EmploymentDetail
        exclude = ['ref']


class SpouseForm(ModelForm):

    class Meta:
        model = SpouseDetail
        exclude = ['ref']


class DependentForm(ModelForm):

    class Meta:
        model = DependentDetail
        exclude = ['ref']