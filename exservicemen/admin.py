from .models import *
from django import forms
from django.contrib import admin
from django.contrib.auth.models import Group
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.forms import ReadOnlyPasswordHashField
from django.core.exceptions import ValidationError

from exservicemen.models import MyUser


class UserCreationForm(forms.ModelForm):
    """A form for creating new users. Includes all the required
    fields, plus a repeated password."""
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Password confirmation', widget=forms.PasswordInput)

    class Meta:
        model = MyUser
        fields = ('email',)

    def clean_password2(self):
        # Check that the two password entries match
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise ValidationError("Passwords don't match")
        return password2

    def save(self, commit=True):
        # Save the provided password in hashed format
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user


class UserChangeForm(forms.ModelForm):
    """A form for updating users. Includes all the fields on
    the user, but replaces the password field with admin's
    password hash display field.
    """
    password = ReadOnlyPasswordHashField()

    class Meta:
        model = MyUser
        fields = ('email', 'password', 'is_active', 'is_admin')

    def clean_password(self):
        # Regardless of what the user provides, return the initial value.
        # This is done here, rather than on the field, because the
        # field does not have access to the initial value
        return self.initial["password"]


class UserAdmin(BaseUserAdmin):
    # The forms to add and change user instances
    form = UserChangeForm
    add_form = UserCreationForm

    # The fields to be used in displaying the User model.
    # These override the definitions on the base UserAdmin
    # that reference specific fields on auth.User.
    list_display = ('email',  'is_admin')
    list_filter = ('is_admin', 'role')
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Permissions', {'fields': ('is_admin', 'role', 'is_active')}),
    )
    # add_fieldsets is not a standard ModelAdmin attribute. UserAdmin
    # overrides get_fieldsets to use this attribute when creating a user.
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2'),
        }),
    )
    search_fields = ('email',)
    ordering = ('email',)
    filter_horizontal = ()


# Now register the new UserAdmin...
admin.site.register(MyUser, UserAdmin)
# ... and, since we're not using Django's built-in permissions,
# unregister the Group model from admin.
admin.site.unregister(Group)


admin.site.register(Service)
admin.site.register(Trade)
admin.site.register(Rank)
admin.site.register(DischargeReason)
admin.site.register(RankCategory)
admin.site.register(PersonalDetail)
admin.site.register(ExServiceMen)
admin.site.register(WidowDetail)
admin.site.register(ServiceDetail)
admin.site.register(State)
admin.site.register(MedicalCategory)
admin.site.register(CasteCategory)
admin.site.register(Character)
admin.site.register(PresentAddress)
admin.site.register(PermanentAddress)
admin.site.register(Department)
admin.site.register(ZilaSainikBoard)
admin.site.register(RajyaSainikBoard)
admin.site.register(CivilQualification)
admin.site.register(District)
admin.site.register(Religion)
admin.site.register(SpouseDetail)
admin.site.register(EmploymentDetail)
admin.site.register(DependentDetail)
admin.site.register(RecordOffice)
# admin.site.register(ApplyDetail)
admin.site.register(TradeGroup)
admin.site.register(PensionDetail)
admin.site.register(WelfareOfficer)
admin.site.register(Director)
admin.site.register(RSBOfficer)
admin.site.register(RSBHead)
admin.site.register(TransferDetail)
admin.site.register(ESMType)
admin.site.register(Corp)
admin.site.register(ServiceNoPrefix)
admin.site.register(ServiceNoSuffix)
admin.site.register(Specialization)
admin.site.register(ESMDocument)