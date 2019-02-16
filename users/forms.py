from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser


class UserSignUpForm(forms.ModelForm):
    password = forms.CharField(widget = forms.PasswordInput)
    username = forms.CharField(widget = forms.TextInput)

    class Meta:
        model = CustomUser
        fields = ['avatar','username', 'password','email']


class UserloginForm(forms.Form):
    username = forms.CharField(widget = forms.TextInput)
    password = forms.CharField(widget = forms.PasswordInput)

    class Meta:
        fields = ['username', 'password']







