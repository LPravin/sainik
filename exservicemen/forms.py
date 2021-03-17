from django import forms
from django.forms import ModelForm
from .models import *
from django.contrib.auth.forms import UserCreationForm, UserChangeForm


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
        }

    # def __init__(self, *args, **kwargs):
    #     super().__init__(*args, **kwargs)
    #
    #     self.fields['trade'].queryset = Trade.objects.none()
    #     self.fields['rank'].queryset = Rank.objects.none()
    #     self.fields['record_office'].queryset = RecordOffice.objects.none()


class PersonalForm(ModelForm):

    class Meta:
        model = PersonalDetail
        exclude = ['ref']


class PensionForm(ModelForm):

    class Meta:
        model = PensionDetail
        exclude = ['ref']




class EmploymentForm(ModelForm):

    class Meta:
        model = EmploymentDetail
        fields = ['civil_qualification', 'test_passed', 'firesafety_sec_qualification',
                  'employment_status', 'willing_for_job', 'security_job',
                       'employer', 'monthly_income', 'department',
                       'civil_retirement_date', 'civil_ppo_no']


class SpouseForm(ModelForm):

    class Meta:
        model = SpouseDetail
        exclude = ['ref']
        fields = ['marital_status', 'marriage_date', 'spouse_relation', 'name', 'dob', 'spouse_qualification',
                  'spouse_employment_status', 'spouse_profession', 'spouse_retirement_date', 'aadhaar_no',
                  'voter_id_no', 'pan_no', 'csd_no', 'echs_no', 'ident_mark_1', 'ident_mark_2', 'next_of_kin',
                  'nok_relation']


class DependentForm(ModelForm):

    class Meta:
        model = DependentDetail
        exclude = ['ref']