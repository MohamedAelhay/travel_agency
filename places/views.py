from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import Country, City, Location, Hotel, CityHotel, UserCityRate, UserCarRent, UserHotelReservation
from .forms import UserCityRateForm, UserCarRentForm, HotelReservationForm
from pprint import *

# Create your views here.


# index Test :-
def index(request):
    countries = getAllCountries()
    context = {"countries": countries }
    return render(request, "index.html", context)


def country_page(request, countryName):
    try:
        country = Country.objects.get(country_Name=countryName)
        cities  = City.objects.filter(country_Name_id=country.id)
        context = {"country": country, "cities": cities}
        return render(request, "country.html", context)
    except:
        return HttpResponseRedirect("/places/")


# Country Methods :-
def getAllCountries():
    countries = Country.objects.all()
    return countries


# City Methods :-
def getAllCities(request):
    cities = City.objects.all()
    context = {"cities": cities}
    return render(request, "citiesPage.html", context)


def getCityById(request, cityId):
    city = City.objects.get(id=eval(cityId))
    context = {"city": city}
    return render(request, "cityPage.html", context)


# Location Methods :-
def getAllLocations(request):
    locations = Location.objects.all()
    context = {"locations": locations}
    return render(request, "locationsPage.html", context)


def getLocationById(request, locationId):
    location = Location.objects.get(id=eval(locationId))
    context = {"location": location}
    return render(request, "locationPage.html", context)


# Hotel Methods :-
def getAllHotels(request):
    hotels = Hotel.objects.all()
    context = {"hotels": hotels}
    return render(request, "hotelsPage.html", context)


def getHotelById(request, hotelId):
    hotel = Hotel.objects.get(id=eval(hotelId))
    context = {"hotel": hotel}
    return render(request, "hotelPage.html", context)


# Services
def getUserCityRate(request, cityId):
    rate = UserCityRate.objects.filter(user_id = request.user.id, city_id = cityId)
    context = {"rate": rate}
    return context


def getUserCarRentals(request, cityId):
    UserCityRatentals = UserCarRent.objects.filter(user_id = request.user.id)
    context = {"rentals": UserCityRatentals}
    return context


def rateCity(request, cityId):
    form = UserCityRateForm(request.POST or None)

    if request.method == 'POST':
        if form.is_valid():
            rate = form.cleaned_data.get('rate')
            try:
                UserCityRate.objects.create(user_id=request.user.id, city_id=cityId, rate=rate)
            except:
                UserCityRate.objects.filter(user_id=request.user.id, city_id=cityId).update(rate =rate)

        return HttpResponseRedirect('/places/cities/rate/')

    else:
        form = UserCityRateForm()
        context = {"form": form}
        return render(request, "rate.html", context)


def rentCar(request):
    form = UserCarRentForm(request.POST or None)

    if request.method == 'POST':
        if form.is_valid():
            # form.save()
            UserCarRent.objects.create(
                user_id        =request.user.id,
                pickup_loc_id  =request.POST.get('pickup_loc'),
                dropoff_loc_id =request.POST.get('dropoff_loc'),
                time           =request.POST.get('time')
            )

        return HttpResponseRedirect('/places/cities/rentCar/')

    else:
        form = UserCarRentForm()
        context = {"form": form}
        return render(request, "rentCar.html", context)


def hotelReservation(request):
    if request.method == 'POST':
        form = HotelReservationForm(request.POST)
        if form.is_valid():
            UserHotelReservation.objects.create(
                user_Name =request.user.id,
                hotel_Name=request.POST.get('hotel_Name'),
                rooms     =request.POST.get('rooms'),
                room_type =request.POST.get('room_type'),
                res_Date  =request.POST.get('res_Time')
            )
            return HttpResponseRedirect('/places/')
    else:
        form = HotelReservationForm()
        context = {'hotel_form': form}
        return render(request, 'hotelReservation.html', context)


# def newCountry(request):
#     if request.method == 'POST':
#         form = CountryForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return HttpResponseRedirect('/places/')
#     else:
#         form = CountryForm()
#         context = {"country_form": form}
#         return render(request, "newCountry.html", context)
#
#
# def editCountry(request, countryId):
#     country = Country.objects.get(id=eval(countryId))
#     if request.method == 'POST':
#         form = CountryForm(request.POST, instance=country)
#         if form.is_valid():
#             form.save()
#             return HttpResponseRedirect("/places/")
#     else:
#         form = CountryForm(instance=country)
#         context = {'country_form': form}
#         return render(request, "newCountry.html", context)
#
#
# def deleteCountry(request, countryId):
#     st = Country.objects.get(id=eval(countryId))
#     st.delete()
#     return HttpResponseRedirect("/places/")






