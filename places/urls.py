from django.conf.urls import url
from places import views

urlpatterns = [
    url(r'^$', views.index),
    # Country Urls:-
    url(r'^countries/$', views.getAllCountries),
    url(r'^(?P<countryId>[0-9]+)/$', views.getCountryById),
    # City Urls:-
    url(r'^cities/$', views.getAllCities),
    url(r'^(?P<cityId>[0-9]+)/$', views.getCityById),
    # Locations Urls:-
    url(r'^locations/$', views.getAllLocations),
    url(r'^(?P<locationId>[0-9]+)/$', views.getLocationById),
    # Hotels Urls:-
    url(r'^hotels/$', views.getAllHotels),
    url(r'^(?P<hotelId>[0-9]+)/$', views.getHotelById),
]




