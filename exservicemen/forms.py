from django import forms
from django.forms import ModelForm
from .models import *
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.core.validators import ValidationError

class CustomUserCreationForm(UserCreationForm):

    class Meta(UserCreationForm):
        model = MyUser
        fields = ('email',)


class CustomUserChangeForm(UserChangeForm):

    class Meta:
        model = MyUser
        fields = ('email',)


class Login(forms.Form):
    username = forms.EmailField(label="Email")
    password = forms.CharField(widget=forms.PasswordInput())


class ApplyForm1(ModelForm):

    class Meta:
        model = ApplyDetail
        exclude = [ 'ref']

        labels = {'basic_reg_type': 'REGISTRATION TYPE', 'zsb': 'previous zsb', 'esm_no': 'ESM NO',
                  'expiry_date': 'DATE OF EXPIRY OF ESM', 'death_certificate': 'DEATH CERTIFICATE',
                  'esm_reg_type': 'ESM REGISTRATION TYPE', 'service': 'SERVICE', 'corps': 'CORPS',
                  'ppo_book': 'PPO BOOK'}

        widgets = {
            'expiry_date': forms.DateInput(attrs={'type': 'date'}),
            'name': forms.TextInput(attrs={'onkeydown': "return alphaOnly(event)", 'onpaste': "return false"}),
            'service_no': forms.TextInput(attrs={'onkeydown': "return numOnly(event)"}),
            'mobile': forms.TextInput(attrs={'onkeydown': "return numOnly(event)"}),
        }

    # def __init__(self, *args, **kwargs):
    #     super().__init__(*args, **kwargs)
    #
    #     self.fields['trade'].queryset = Trade.objects.none()
    #     self.fields['rank'].queryset = Rank.objects.none()
    #     self.fields['record_office'].queryset = RecordOffice.objects.none()

    def clean(self):
        # data from the form is fetched using super function
        super(ApplyForm1, self).clean()
        brt = self.cleaned_data.get('basic_reg_type')
        name = self.cleaned_data.get('name')
        zsb = self.cleaned_data.get('zsb')
        expiry_date = self.cleaned_data.get('expiry_date')
        esm_no = self.cleaned_data.get('esm_no')
        ert = self.cleaned_data.get('esm_reg_type')
        service = self.cleaned_data.get('service')
        corps = self.cleaned_data.get('corps')
        record_office = self.cleaned_data.get('record_office')
        group = self.cleaned_data.get('group')
        trade = self.cleaned_data.get('trade')
        rank_category = self.cleaned_data.get('rank_category')
        rank = self.cleaned_data.get('rank')
        state = self.cleaned_data.get('state')
        district = self.cleaned_data.get('district')

        if not brt:
            self._errors['basic_reg_type'] = self.error_class([
                'Basic registration type must be selected'])
        if not name:
            self._errors['name'] = self.error_class(['Name cannot be left blank'])

        if brt == 'E' or brt == 'TE' or brt == 'EW':
            if not ert:
                self._errors['esm_reg_type'] = self.error_class([
                    'ESM Registration type must be selected'])
            if not service:
                self._errors['service'] = self.error_class([
                    'Service must be selected'])
            if service == "2":
                if not corps:
                    self._errors['corps'] = self.error_class([
                        'Corps must be selected'])
            if not record_office:
                self._errors['record_office'] = self.error_class([
                    'Record office must be selected'])
            if not group:
                self._errors['group'] = self.error_class([
                    'Group must be selected'])
            if not trade:
                self._errors['trade'] = self.error_class([
                    'Trade must be selected'])
            if not rank_category:
                self._errors['rank_category'] = self.error_class([
                    'Rank category must be selected'])
            if not rank:
                self._errors['rank'] = self.error_class([
                    'Rank must be selected'])

        if brt == 'W' or brt == 'TE':
            if not esm_no:
                self._errors['esm_no'] = self.error_class([
                    'ESM No cannot be blank'])

        if brt == "W" or brt == 'EW':
            if not expiry_date:
                self._errors['expiry_date'] = self.error_class([
                    'Expiry date cannot be blank'])

        if not state:
            self._errors['state'] = self.error_class([
                'State must be selected'])

        if not district:
            self._errors['district'] = self.error_class([
                'District must be selected'])


class ServiceForm(ModelForm):

    class Meta:
        model = ServiceDetail
        exclude = ['ref']


class PersonalForm(ModelForm):

    class Meta:
        model = PersonalDetail
        exclude = ['ref']

        widgets = {
            'dob': forms.DateInput(attrs={'type': 'date'}),
            'name': forms.TextInput(attrs={'onkeydown': "return alphaOnly(event)"}),
            'father': forms.TextInput(attrs={'onkeydown': "return alphaOnly(event)"}),
            'mother': forms.TextInput(attrs={'onkeydown': "return alphaOnly(event)"}),
            'aadhaar_no': forms.TextInput(attrs={'onkeydown': "return numOnly(event)"}),
            'expiry_date': forms.DateInput(attrs={'type': 'date'}),
            }


class PensionForm(ModelForm):

    class Meta:
        model = PensionDetail
        exclude = ['ref']

        widgets = {
            'discharge_date': forms.DateInput(attrs={'type': 'date'}),
            'disability_percent': forms.NumberInput(attrs={'onkeydown': "return numOnly(event)"})
            }


class EmploymentForm(ModelForm):

    class Meta:
        model = EmploymentDetail
        fields = ['civil_qualification', 'test_passed', 'firesafety_sec_qualification',
                  'employment_status', 'willing_for_job', 'security_job',
                  'employer', 'monthly_income', 'department', 'civil_retirement_date', 'civil_ppo_no']


class SpouseForm(ModelForm):

    class Meta:
        model = SpouseDetail
        exclude = ['ref']
        fields = ['marital_status', 'marriage_date', 'spouse_relation', 'name', 'dob', 'spouse_qualification',
                  'spouse_employment_status', 'spouse_profession', 'spouse_retirement_date', 'aadhaar_no',
                  'voter_id_no', 'pan_no', 'csd_no', 'echs_no', 'ident_mark_1', 'ident_mark_2', 'next_of_kin',
                  'nok_relation']

        widgets = {
            'dob': forms.DateInput(attrs={'type': 'date'}),
            'name': forms.TextInput(attrs={'onkeydown': "return alphaOnly(event)"}),
            'aadhaar_no': forms.TextInput(attrs={'onkeydown': "return numOnly(event)"}),
            'marriage_date': forms.DateInput(attrs={'type': 'date'}),
            'spouse_retirement_date': forms.DateInput(attrs={'type': 'date'}),
        }


class DependentForm(ModelForm):

    class Meta:
        model = DependentDetail
        exclude = ['ref']

        widgets = {
            'dep_dob': forms.DateInput(attrs={'type': 'date'})
        }
