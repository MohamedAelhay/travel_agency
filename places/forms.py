from django import forms
from .models import UserCityRate, UserCarRent
from django.forms.widgets import SplitDateTimeWidget
from django.forms import SplitDateTimeField

class UserCityRateForm(forms.ModelForm):
    class Meta:
        model  = UserCityRate
        fields = ['rate']

class UserCarRentForm(forms.ModelForm):
    time= forms.DateField(widget=forms.SelectDateWidget())

    class Meta:
        model  = UserCarRent
        fields = ['pickup_loc','dropoff_loc', 'time']
