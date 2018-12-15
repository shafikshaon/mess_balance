from django.forms import forms

from accounts.models import User


class LoginForm(forms.Form):
    class Meta:
        model = User
        fields = ('username', 'password')
