from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import Country, City, Location, Hotel, CityHotel

# Create your views here.


# index Test :-
def index(request):
    return HttpResponse("<h1>Hello Places</h1>")


# Country Methods :-
def getAllCountries(request):
    countries = Country.objects.all()
    context = {"countries": countries}
    # return HttpResponse(countries)
    return render(request, "countriesPage.html", context)


def getCountryById(request, countryId):
    country = Country.objects.get(id=eval(countryId))
    context = {"country": country}
    return render(request, "countryPage.html", context)


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






