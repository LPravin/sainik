from django import forms
from django.forms import ModelForm
from .models import *
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import MyUser


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
    have_esm = forms.CharField(required=True)

    class Meta:
        model = ApplyDetail
        exclude = ['mail', 'mobile', 'password', 'confirm_password', 'ref']
        field_order = ['name', 'basic_reg_type', 'have_esm', 'esm_no', 'expiry_date', 'esm_reg_type', 'service',
                       'corps', 'records', 'group', 'trade', 'rank_category', 'rank', 'service_no', 'state', 'district',
                       'discharge_book', 'ppo_book', 'residence_certificate', 'death_certificate']

        labels = {'basic_reg_type': 'REGISTRATION TYPE', 'have_esm': 'DO YOU HAVE ESM ID?', 'esm_no': 'ESM NO',
                   'expiry_date': 'DATE OF EXPIRY OF ESM', 'death_certificate': 'DEATH CERTIFICATE',
                   'esm_reg_type': 'EXSERVICEMEN REGISTRATION TYPE', 'service': 'SERVICE', 'corps': 'CORPS',
                   'ppo_book': 'PPO BOOK'}

    # def clean(self):
    #     cleaned_data = super().clean()
    #     cc_myself = cleaned_data.get("cc_myself")
    #     subject = cleaned_data.get("subject")


# class ServiceForm(ModelForm):
#
#     class Meta:
#         model = ServiceDetail
#         exclude = ['zila_board_id', 'ref']
#         widgets = {
#             'reg_date': forms.DateInput(attrs={'type': 'date'}),
#         }


class PersonalForm(ModelForm):

    class Meta:
        model = PersonalDetail
        exclude = ['ref']


class DischargeForm(ModelForm):

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