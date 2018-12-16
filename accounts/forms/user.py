from django import forms

from accounts.models import User


class AddUserForm(forms.ModelForm):
    first_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    last_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    email = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    is_superuser = forms.BooleanField(widget=forms.CheckboxInput(attrs={'class': ''}), required=False)
    is_staff = forms.BooleanField(widget=forms.CheckboxInput(attrs={'class': ''}), required=False)
    is_user = forms.BooleanField(widget=forms.CheckboxInput(attrs={'class': ''}), required=False)
    is_admin = forms.BooleanField(widget=forms.CheckboxInput(attrs={'class': ''}), required=False)
    is_active = forms.BooleanField(widget=forms.CheckboxInput(attrs={'class': ''}), required=False)

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'username', 'email', 'password', 'is_superuser', 'is_staff', 'is_user',
                  'is_admin', 'is_active')


class UpdateUserForm(forms.ModelForm):
    first_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    last_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    email = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    is_superuser = forms.BooleanField(widget=forms.CheckboxInput(attrs={'class': ''}), required=False)
    is_staff = forms.BooleanField(widget=forms.CheckboxInput(attrs={'class': ''}), required=False)
    is_user = forms.BooleanField(widget=forms.CheckboxInput(attrs={'class': ''}), required=False)
    is_admin = forms.BooleanField(widget=forms.CheckboxInput(attrs={'class': ''}), required=False)
    is_active = forms.BooleanField(widget=forms.CheckboxInput(attrs={'class': ''}), required=False)

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'username', 'email', 'password', 'is_superuser', 'is_staff', 'is_user',
                  'is_admin', 'is_active')
