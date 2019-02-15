from django.contrib import admin
from .models import Country, City, Location, Hotel, CityHotel
# Register your models here.
# Super User
# user: 'mohamed'
# email:'cap.mohamed.abdelhay@gmail.com'
# pass: 'Os@12345'


class CustomCountry(admin.ModelAdmin):
    fieldsets = [
        ['Country Info', {'fields': ['country_Name']}],
        ['Cities', {'fields': ['country_Name']}]
    ]
    list_display = ['country_Name']
    list_filter = ['country_Name']
    search_fields = ['country_Name']


class CustomCity(admin.ModelAdmin):
    fieldsets = [
        ['City Info', {'fields': ['city_Name', 'description']}],
        ['Cities', {'fields': ['country_Name']}]
    ]
    list_display = ['city_Name', 'city_Description']
    list_filter = ['country_Name__country_Name']
    search_fields = ['city_Name']


class CustomLocation(admin.ModelAdmin):
    fieldsets = [
        ['Location Info', {'fields': ['loc_Name']}],
        ['City', {'fields': ['city_Name']}]
    ]
    list_display = ['loc_Name', 'city_Name']
    list_filter = ['city_Name__city_Name']
    search_fields = ['city_Name', 'loc_Name']


class CustomHotel(admin.ModelAdmin):
    fieldsets = [
        ['Hotel Info', {'fields': ['hotel_Name']}],
        ['City', {'fields': ['city_Name']}]
    ]
    list_display = ['hotel_id', 'city_id']
    list_filter = ['hotel_id__hotel_Name', 'city_id__city_Name']
    search_fields = ['city_id', 'hotel_id']


# myModels = [Country, City]
admin.site.register(Country, CustomCountry)
admin.site.register(City, CustomCity)
admin.site.register(Location, CustomLocation)
admin.site.register(CityHotel, CustomHotel)





