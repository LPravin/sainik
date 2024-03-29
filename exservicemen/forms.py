from django import forms
from django.forms import ModelForm
from .models import *
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.core.validators import ValidationError
import datetime


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


# class ApplyForm1(ModelForm):
#
#     class Meta:
#         model = ApplyDetail
#         exclude = [ 'ref']
#
#         labels = {'basic_reg_type': 'REGISTRATION TYPE', 'zsb': 'previous zsb', 'esm_no': 'ESM NO',
#                   'expiry_date': 'DATE OF EXPIRY OF ESM', 'death_certificate': 'DEATH CERTIFICATE',
#                   'esm_reg_type': 'ESM REGISTRATION TYPE', 'service': 'SERVICE', 'corps': 'CORPS',
#                   'ppo_book': 'PPO BOOK'}
#
#         widgets = {
#             'expiry_date': forms.DateInput(attrs={'type': 'date'}),
#             'name': forms.TextInput(attrs={'onkeydown': "return alphaOnly(event)", 'onpaste': "return false",
#                                            "style": "text-transform: uppercase;"}),
#             'service_no': forms.TextInput(attrs={'onkeydown': "return numOnly(event)"}),
#             'mobile': forms.TextInput(attrs={'onkeydown': "return numOnly(event)"}),
#         }
#
    # def __init__(self, *args, **kwargs):
#     #     super().__init__(*args, **kwargs)
#     #     self.fields['record_office'].queryset = RecordOffice.objects.none()
#     #     self.fields['trade'].queryset = Trade.objects.none()
#     #     self.fields['rank'].queryset = Rank.objects.none()
#     #     self.fields['district'].queryset = District.objects.none()
#     #
#     #     if 'service' in self.data:
#     #         try:
#     #             service_id = int(self.data.get('service'))
#     #             self.fields['record_office'].queryset = RecordOffice.objects.filter(service_id=service_id).order_by(
#     #                 'record_office_name')
#     #         except (ValueError, TypeError):
#     #             pass  # invalid input from the client; ignore and fallback to empty City queryset
#     #     elif self.instance.pk:
#     #         self.fields['record_office'].queryset = self.instance..order_by('record_office_name')
#     #
#     #     if 'service' and 'group' in self.data:
#     #         try:
#     #             service_id = int(self.data.get('service'))
#     #             group_id = int(self.data.get('group'))
#     #             self.fields['trade'].queryset = Trade.objects.filter(service_id=service_id, trade_group_id=group_id).order_by(
#     #                 'trade_group')
#     #         except (ValueError, TypeError):
#     #             pass  # invalid input from the client; ignore and fallback to empty City queryset
#     #     elif self.instance.pk:
#     #         self.fields['group'].queryset = self.instance.service.order_by('trade_group')
#     #
#     #     if 'rank_category' in self.data:
#     #         try:
#     #             rank_category_id = int(self.data.get('rank_category'))
#     #             self.fields['rank'].queryset = Rank.objects.filter(rank_category=rank_category_id).order_by(
#     #                 'rank')
#     #         except (ValueError, TypeError):
#     #             pass  # invalid input from the client; ignore and fallback to empty City queryset
#     #     elif self.instance.pk:
#     #         self.fields['rank'].queryset = self.instance.service.order_by('rank_category')
#     #
#     #     if 'state' in self.data:
#     #         try:
#     #             state_id = int(self.data.get('state_id'))
#     #             self.fields['state_id'].queryset = District.objects.filter(rank_category=state_id).order_by(
#     #                 'district_name')
#     #         except (ValueError, TypeError):
#     #             pass  # invalid input from the client; ignore and fallback to empty City queryset
#     #     elif self.instance.pk:
#     #         self.fields['district'].queryset = self.instance.service.order_by('district_name')
#
#     def clean(self):
#         # data from the form is fetched using super function
#         super(ApplyForm1, self).clean()
#         brt = self.cleaned_data.get('basic_reg_type')
#         name = self.cleaned_data.get('name')
#         zsb = self.cleaned_data.get('zsb')
#         expiry_date = self.cleaned_data.get('expiry_date')
#         esm_no = self.cleaned_data.get('esm_no')
#         ert = self.cleaned_data.get('esm_reg_type')
#         service = self.cleaned_data.get('service')
#         corps = self.cleaned_data.get('corps')
#         record_office = self.cleaned_data.get('record_office')
#         group = self.cleaned_data.get('group')
#         trade = self.cleaned_data.get('trade')
#         rank_category = self.cleaned_data.get('rank_category')
#         rank = self.cleaned_data.get('rank')
#         state = self.cleaned_data.get('state')
#         district = self.cleaned_data.get('district')
#
#         if not brt:
#             self._errors['basic_reg_type'] = self.error_class([
#                 'Basic registration type must be selected'])
#         if not name:
#             self._errors['name'] = self.error_class(['Name cannot be left blank'])
#
#         if brt == 'E' or brt == 'TE' or brt == 'EW':
#             if not ert:
#                 self._errors['esm_reg_type'] = self.error_class([
#                     'ESM Registration type must be selected'])
#             if not service:
#                 self._errors['service'] = self.error_class([
#                     'Service must be selected'])
#             if service == "2":
#                 if not corps:
#                     self._errors['corps'] = self.error_class([
#                         'Corps must be selected'])
#             if not record_office:
#                 self._errors['record_office'] = self.error_class([
#                     'Record office must be selected'])
#             if not group:
#                 self._errors['group'] = self.error_class([
#                     'Group must be selected'])
#             if not trade:
#                 self._errors['trade'] = self.error_class([
#                     'Trade must be selected'])
#             if not rank_category:
#                 self._errors['rank_category'] = self.error_class([
#                     'Rank category must be selected'])
#             if not rank:
#                 self._errors['rank'] = self.error_class([
#                     'Rank must be selected'])
#
#         if brt == 'W' or brt == 'TE':
#             if not esm_no:
#                 self._errors['esm_no'] = self.error_class([
#                     'ESM No cannot be blank'])
#
#         if brt == "W" or brt == 'EW':
#             if not expiry_date:
#                 self._errors['expiry_date'] = self.error_class([
#                     'Expiry date cannot be blank'])
#
#         if not state:
#             self._errors['state'] = self.error_class([
#                 'State must be selected'])
#
#         if not district:
#             self._errors['district'] = self.error_class([
#                 'District must be selected'])


class ServiceForm(ModelForm):

    class Meta:
        model = ServiceDetail
        exclude = ['ref']
        widgets = {
            'reg_date': forms.DateInput(attrs={'type': 'date', 'max': str(datetime.date.today())}),
            'enrollment_date': forms.DateInput(attrs={'type': 'date', 'max': str(datetime.date.today())}),
            'name': forms.TextInput(attrs={"style": "text-transform: uppercase;",
                                           'onkeydown': "return alphaOnly(event)",
                                           'onpaste': "return false"}),

            'dob': forms.DateInput(attrs={'type': 'date', 'max': datetime.date(datetime.date.today().year - 15,
                                                                               datetime.date.today().month,
                                                                               datetime.date.today().day)}),
            'mobile': forms.TextInput(attrs={'onkeydown': "return numOnly(event)",
                                             'onpaste': "return false"}),
            'other_rank': forms.TextInput(attrs={"style": "text-transform: uppercase;",
                                                 'onkeydown': "return alphaOnly(event)"}),
            'other_trade': forms.TextInput(attrs={"style": "text-transform: uppercase;",
                                                  'onkeydown': "return alphaOnly(event)"}),
            "prefix": forms.Select(attrs={'style': "width:40%; margin-right: 3px;"}),
            "suffix": forms.Select(attrs={'style': "width:30%; margin-right: 3px;"}),
            'service_no': forms.TextInput(attrs={'onkeydown': "return numOnly(event)",
                                                 'onpaste': "return false"})
            # attrs = {'mindate': '2021-03-27'}
        }

    def clean_name(self):
        name = self.cleaned_data['name'].upper()
        return name

    def clean_mobile(self):
        mobile = self.cleaned_data['mobile']
        if len(mobile) != 10:
            raise ValidationError("Mobile number must be 10 digits")
        if not mobile.isdigit():
            raise ValidationError("Invalid Mobile Number")
        return mobile


class PersonalForm(ModelForm):

    class Meta:
        model = PersonalDetail
        exclude = ['ref']

        widgets = {
            'father': forms.TextInput(attrs={'onkeydown': "return alphaOnly(event)",
                                             "style": "text-transform: uppercase;"}),
            'mother': forms.TextInput(attrs={'onkeydown': "return alphaOnly(event)",
                                             "style": "text-transform: uppercase;"}),
            'aadhaar_no': forms.TextInput(attrs={'onkeydown': "return numOnly(event)"}),
            'birth_place': forms.TextInput(attrs={'onkeydown': "return alphaOnly(event)",
                                                  "style": "text-transform: uppercase;"}),
            'expiry_date': forms.DateInput(attrs={'type': 'date'}),
            }

    def clean_father(self):
        father = self.cleaned_data['father'].upper()
        return father

    def clean_mother(self):
        mother = self.cleaned_data['mother'].upper()
        return mother

    def clean_birth_place(self):
        bp = self.cleaned_data['birth_place'].upper()
        return bp


class PensionForm(ModelForm):

    class Meta:
        model = PensionDetail
        fields = ['unit_last_served', 'discharge_date', 'discharge_reason', 'medical_category', 'character',
                  'discharge_book_no', 'ppo_no', 'pensioner_status', 'pension_sanctioned', 'present_pension',
                  'whether_pwd', 'disability_pension', 'disability_percent', 'family_pension']

        widgets = {
            'discharge_date': forms.DateInput(attrs={'type': 'date'}),
            'disability_percent': forms.TextInput(attrs={'onkeydown': "return numOnly(event)"}),
            'unit_last_served': forms.TextInput(attrs={"style": "text-transform: uppercase;"})
            }

    def clean_unit_last_served(self):
        uls = self.cleaned_data['unit_last_served'].upper()
        return uls

    # def clean_ppo_no(self):
    #     p_status = self.cleaned_data['pensioner_status']
    #     ppo_number = self.cleaned_data['ppo_no']
    #     if p_status == 'Y':
    #         if not ppo_number:
    #             raise ValidationError('PPO Number cannot be blank')

    def clean(self):
        cleaned_data = super().clean()
        p = cleaned_data.get("pensioner_status")
        pwd_s = cleaned_data.get('whether_pwd')
        ppo = cleaned_data.get("ppo_no")
        ps = cleaned_data.get('pension_sanctioned')
        pp = cleaned_data.get('present_pension')
        dp = cleaned_data.get('disability_pension')
        dper = cleaned_data.get('disability_percent')

        if p == "Y":
            if not ppo:
                msg = 'PPO Number cannot be blank'
                self.add_error('ppo_no', msg)
            elif not ps:
                msg = 'This field is required'
                self.add_error('pension_sanctioned', msg)
            elif not pp:
                msg = 'This field is required'
                self.add_error('present_pension', msg)
        if pwd_s == "Y":
            if not dp:
                msg = 'This field is required'
                self.add_error('disability_pension', msg)
            elif not dper:
                msg = 'This field is required'
                self.add_error('disability_percent', msg)


class EmploymentForm(ModelForm):

    class Meta:
        model = EmploymentDetail
        fields = ['civil_qualification', 'specialization','test_passed',
                  'employment_status', 'willing_for_job', 'security_job', 'sector',
                   'monthly_income', 'department', 'civil_retirement_date', 'civil_ppo_no']

        widgets = {
            'civil_retirement_date': forms.DateInput(attrs={'type': 'date'}),
        }


class SpouseForm(ModelForm):

    class Meta:
        model = SpouseDetail
        exclude = ['ref']
        fields = ['marital_status', 'marriage_date', 'spouse_relation', 'spouse_name', 'dob', 'spouse_qualification',
                  'spouse_employment_status', 'spouse_profession', 'spouse_retirement_date', 'aadhaar_no',
                  'voter_id_no', 'pan_no', 'csd_no', 'echs_no', 'ident_mark_1', 'ident_mark_2', 'next_of_kin',
                  'nok_relation']

        widgets = {
            'dob': forms.DateInput(attrs={'type': 'date'}),
            'spouse_name': forms.TextInput(attrs={'onkeydown': "return alphaOnly(event)", }),
            'aadhaar_no': forms.TextInput(attrs={'onkeydown': "return numOnly(event)"}),
            'marriage_date': forms.DateInput(attrs={'type': 'date'}),
            'spouse_retirement_date': forms.DateInput(attrs={'type': 'date'}),
        }

    def clean_spouse_name(self):
        ms = self.cleaned_data['marital_status']
        sn = self.cleaned_data['spouse_name']
        if ms == "M":
            if not sn:
                raise ValidationError('Spouse name cannot be blank')


class DependentForm(ModelForm):

    class Meta:
        model = DependentDetail
        exclude = ['ref']

        widgets = {
            'dep_dob': forms.DateInput(attrs={'type': 'date'}),
            'dep_name': forms.TextInput(attrs={'onkeydown': "return alphaOnly(event)",
                                               "style": "text-transform: uppercase;"}),
            'aadhaar_no': forms.TextInput(attrs={'onkeydown': "return numOnly(event)", 'minlength': '12'}),

            'academic_year': forms.TextInput(attrs={'onkeydown': "return numOnly(event)"}),
        }

    def clean_dep_name(self):
        dep = self.cleaned_data['dep_name'].upper()
        return dep


class ContactForm1(ModelForm):
    class Meta:
        model = PermanentAddress
        exclude = ['ref']

        widgets = {
            'is_address_same': forms.CheckboxInput(),
            'house_no': forms.TextInput(attrs={'class':'cf1'}),
            'house_name': forms.TextInput(attrs={'class': 'cf1', 'onkeydown': "return alphaOnly(event)"}),
            'street_name': forms.TextInput(attrs={'class': 'cf1'}),
            'city': forms.TextInput(attrs={'class': 'cf1', 'onkeydown': "return alphaOnly(event)"}),
            'district': forms.Select(attrs={'class': 'cf1'}),
            'state': forms.Select(attrs={'class': 'cf1'}),
            'pincode': forms.TextInput(attrs={'class': 'cf1', 'minlength': '6', 'onkeydown': "return numOnly(event)"}),
            'telephone': forms.TextInput(attrs={'onkeydown': "return numOnly(event)"})
        }


class ContactForm2(ModelForm):
    class Meta:
        model = PresentAddress
        exclude = ['ref']

        widgets = {
            'house_no': forms.TextInput(attrs={'id': "hno"}),
            'house_name': forms.TextInput(attrs={'id': "hname"}),
            'street_name': forms.TextInput(attrs={'id': "sname"}),
            'city': forms.TextInput(attrs={'id': "city"}),
            'district': forms.Select(attrs={'id': "district"}),
            'state': forms.Select(attrs={'id': "state"}),
            'pincode': forms.TextInput(attrs={'id': "pincode", 'minlength': '6', 'onkeydown': "return numOnly(event)"}),
        }


class ESMBasic(ModelForm):
    esm_no = forms.CharField(max_length=4, widget=forms.TextInput(attrs={'onkeydown': "return numOnly(event)"}))

    class Meta:
        model = ExServiceMen
        fields = ['esm_no', 'reg_category']


class TransferForm(ModelForm):
    class Meta:
        model = TransferDetail
        exclude = ['ref']


class WidowForm(ModelForm):
    expiry_date = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))
    spouse_esm_no = forms.CharField(max_length=4, widget=forms.TextInput(attrs={'onkeydown': "return numOnly(event)"}))

    class Meta:
        model = WidowDetail
        exclude = ['ref']
        widgets = {
            'widow_expiry_date': forms.DateInput(attrs={'type': 'date'})
        }


class ESMDocumentForm(ModelForm):

    class Meta:
        model = ESMDocument
        exclude = ['ref']


class SpouseDocumentForm(ModelForm):

    class Meta:
        model = SpouseDetail
        fields = ['aadhaar_card', 'pan_card', 'echs_card', 'voter_id']


class DependentDocumentForm(ModelForm):

    class Meta:
        model = DependentDetail
        fields = ['aadhaar_card', 'pan_card', 'echs_card', 'voter_id']


class FilterForm(forms.Form):
    reg_categories = (
        ('', '---------'),
        (1, 'ESM'),
        (2, 'WIDOW'),
        (3, 'WIDOW IN SERVICE / UNREGISTERED')
    )
    EStates = [
        ('', '---------'),
        ('E', 'EMPLOYED'),
        ('U', 'UNEMPLOYED'),
        ('R', 'RETIRED')
    ]
    date_choices = [
        ('', '---------'),
        (1, 'ON'),
        (2, 'AFTER'),
        (3, 'BEFORE'),
        (4, 'ON OR AFTER'),
        (5, 'ON OR BEFORE')
    ]
    YesNo = [
        ('', '---------'),
        ('Y', 'Yes'),
        ('N', 'No')
    ]
    MaritalStates = [
        ('', '---------'),
        ('S', 'SINGLE'),
        ('M', 'MARRIED'),
        ('D', 'DIVORCED'),
        ('W', 'WIDOWER')
    ]
    name_contains = forms.CharField(widget=forms.TextInput, required=False)
    registration_types = forms.ChoiceField(widget=forms.Select, choices=reg_categories, required=False)
    services = forms.ModelChoiceField(queryset=Service.objects.all(), required=False)
    esm_type = forms.ModelChoiceField(queryset=ESMType.objects.all(), required=False)
    trades = forms.ModelChoiceField(queryset=Trade.objects.all(), required=False)
    rank_categories = forms.ModelChoiceField(queryset=RankCategory.objects.all(), required=False)
    record_offices = forms.ModelChoiceField(queryset=RecordOffice.objects.all(), required=False)
    employment_status = forms.ChoiceField(widget=forms.Select, choices=EStates, required=False)
    employment_registration = forms.ChoiceField(widget=forms.Select, choices=YesNo, required=False)
    security_job = forms.ChoiceField(widget=forms.Select, choices=YesNo, required=False)
    civil_qualifications = forms.ModelChoiceField(queryset=CivilQualification.objects.all(), required=False)
    dob_date = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}), required=False)
    age_completed = forms.CharField(widget=forms.NumberInput, required=False)
    enrollment_date = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}), required=False)
    ed_conditions = forms.ChoiceField(widget=forms.Select, choices=date_choices, required=False)
    date_of_discharge = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}), required=False)
    dod_conditions = forms.ChoiceField(widget=forms.Select, choices=date_choices, required=False)
    marital_status = forms.ChoiceField(widget=forms.Select, choices=MaritalStates, required=False)
    city = forms.CharField(widget=forms.TextInput, required=False)
    district = forms.ModelChoiceField(queryset=District.objects.all(), required=False)
    state = forms.ModelChoiceField(queryset=State.objects.all(), required=False)
# class FilterService(ModelForm):
#     service = forms.ModelMultipleChoiceField(widget=forms.CheckboxSelectMultiple(), queryset=Service.objects.all())
#
#     class Meta:
#         model = ServiceDetail
#         fields = ['name', 'dob', 'enrollment_date', 'trade', 'service', 'rank_category']