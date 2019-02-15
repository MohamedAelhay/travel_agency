from django.db import models

# Create your models here.


class Country(models.Model):
    country_Name = models.CharField(max_length=100)
    country_Pic = models.CharField(max_length=300)

    def __str__(self):
        return self.country_Name

    class Meta:
        verbose_name_plural = "Countries"


class City(models.Model):
    city_Name = models.CharField(max_length=100)
    city_Description = models.CharField(max_length=1000)
    city_Pic = models.CharField(max_length=300)
    country_Name = models.ForeignKey(Country)

    def __str__(self):
        return self.city_Name

    class Meta:
        verbose_name_plural = "Cities"


class Location(models.Model):
    loc_Name = models.CharField(max_length=100)
    loc_Description = models.CharField(max_length=1000, null=True, blank=True)
    loc_Pic = models.CharField(max_length=300)
    city_Name = models.ForeignKey(City)

    def __str__(self):
        return self.loc_Name


class Hotel(models.Model):
    hotel_Name = models.CharField(max_length=100)
    hotel_Pic = models.CharField(max_length=300)

    def __str__(self):
        return self.hotel_Name


class CityHotel(models.Model):
    city_id = models.ForeignKey(City)
    hotel_id = models.ForeignKey(Hotel)

    class Meta:
        verbose_name_plural = "Hotels"












