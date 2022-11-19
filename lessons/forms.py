from django import forms
from django.core.validators import RegexValidator
from .models import User

class LogInForm(forms.Form):
    username = forms.CharField(label='Username', max_length=50)
    password = forms.CharField(label='Password', max_length=50, widget=forms.PasswordInput)