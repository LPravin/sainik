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

    class Meta:
        model = ApplyDetail
        exclude = ['mail', 'mobile', 'password', 'confirm_password', 'ref']
        field_order = ['name', 'basic_reg_type', 'have_esm', 'esm_no', 'expiry_date', 'death_certificate',
                       'esm_reg_type', 'service', 'corps', 'records', 'group', 'trade', 'rank_category',
                       'rank', 'service_no', 'state', 'district', 'discharge_book', 'ppo_book', 'residence_certificate']

        labels = { 'basic_reg_type': 'REGISTRATION TYPE', 'have_esm': 'DO YOU HAVE ESM ID?','esm_no': 'ESM NO',
                   'expiry_date': 'DATE OF EXPIRY OF ESM', 'death_certificate': 'DEATH CERTIFICATE',
                   'esm_reg_type': 'EXSERVICEMEN REGISTRATION TYPE', 'service': 'SERVICE', 'corps': 'CORPS',
                   'ppo_book': 'PPO BOOK'}

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['record_office'].queryset = RecordOffice.objects.none()
        self.fields['trade'].queryset = Trade.objects.none()

        if 'service' in self.data:
            try:
                service_id = int(self.data.get('service'))
                self.fields['record_office'].queryset = RecordOffice.objects.filter(service_id=service_id).order_by('record_office_name')
            except (ValueError, TypeError):
                pass  # invalid input from the client; ignore and fallback to empty City queryset
        elif self.instance.pk:
            self.fields['record_office'].queryset = self.instance.service.city_set.order_by('record_office_name')

        if 'service' and 'group' in self.data:
            try:
                service_id = int(self.data.get('service'))
                group_id = int(self.data.get('group'))
                self.fields['trade'].queryset = Trade.objects.filter(service_id=service_id, group_id=group_id).order_by(
                    'trade_group')
            except (ValueError, TypeError):
                pass  # invalid input from the client; ignore and fallback to empty City queryset
        elif self.instance.pk:
            self.fields['group'].queryset = self.instance.service.city_set.order_by('trade_group')




'''class ApplyForm2(ModelForm):

    confirm_password = forms.CharField(max_length=16)

    class Meta:
        model = User
        fields = ['username', 'email', 'password', 'confirm_password']
        labels = {
            'username': 'Name'
        }'''


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