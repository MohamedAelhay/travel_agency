from django import forms
from django.http import request

from .models import UserCityRate, UserCarRent, UserHotelReservation
from django.forms.widgets import SplitDateTimeWidget
from django.forms import SplitDateTimeField


class UserCityRateForm(forms.ModelForm):
    class Meta:
        model = UserCityRate
        fields = ['rate']


class UserCarRentForm(forms.ModelForm):
    time = forms.SplitDateTimeWidget

    class Meta:
        model = UserCarRent
        fields = ['pickup_loc', 'dropoff_loc', 'time']


class HotelReservationForm(forms.ModelForm):
    from_Date = forms.DateField(widget=forms.SelectDateWidget)
    to_Date = forms.DateField(widget=forms.SelectDateWidget)

    class Meta:
        model = UserHotelReservation
        fields = ['hotel_Name', 'rooms', 'room_type', 'to_Date', 'from_Date']

