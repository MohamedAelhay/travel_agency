from django import forms
from django.contrib.auth.models import User
# Create your models here.

class UserSignUpForm(forms.ModelForm):
    password = forms.CharField(widget = forms.PasswordInput)
    username = forms.CharField(widget = forms.TextInput)

    class Meta:
        model = User
        fields = ['username','email', 'password']

class UserloginForm(forms.Form):
    username = forms.CharField(widget = forms.TextInput)
    password = forms.CharField(widget = forms.PasswordInput)

    class Meta:
        fields = ['username', 'password']