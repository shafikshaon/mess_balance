import datetime

from django import forms
from django.utils.translation import gettext as _

from accounts.models import User

current_year = str(datetime.date.today().year)
next_year = str(datetime.date.today().year + 1)

MONTHS = {
    1: _('Jan'), 2: _('Feb'), 3: _('Mar'), 4: _('Apr'),
    5: _('May'), 6: _('Jun'), 7: _('Jul'), 8: _('Aug'),
    9: _('Sep'), 10: _('Oct'), 11: _('Nov'), 12: _('Dec')
}


class AddUserForm(forms.ModelForm):
    member_from = forms.DateField(
        widget=forms.SelectDateWidget(
            years=(current_year, next_year),
            months=MONTHS,
            attrs={'class': 'form-control d-inline w-30 mr-2'}),
        initial=datetime.datetime.now)
    first_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    last_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    email = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    phone_number = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}), required=False)
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    is_superuser = forms.BooleanField(widget=forms.CheckboxInput(attrs={'class': ''}), required=False)
    is_admin = forms.BooleanField(widget=forms.CheckboxInput(attrs={'class': ''}), required=False)

    class Meta:
        model = User
        fields = (
            'member_from', 'first_name', 'last_name', 'username', 'email', 'phone_number', 'password', 'is_superuser',
            'is_admin')


class UpdateUserForm(forms.ModelForm):
    member_from = forms.DateField(
        widget=forms.SelectDateWidget(
            years=(current_year, next_year),
            months=MONTHS,
            attrs={'class': 'form-control d-inline w-30 mr-2'}),
        initial=datetime.datetime.now)
    first_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    last_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    email = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    phone_number = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}), required=False)
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    is_superuser = forms.BooleanField(widget=forms.CheckboxInput(attrs={'class': ''}), required=False)
    is_admin = forms.BooleanField(widget=forms.CheckboxInput(attrs={'class': ''}), required=False)
    is_active = forms.BooleanField(widget=forms.CheckboxInput(attrs={'class': ''}), required=False)

    class Meta:
        model = User
        fields = ('member_from', 'first_name', 'last_name', 'username', 'email', 'phone_number', 'password',
                  'is_superuser',
                  'is_admin', 'is_active')
