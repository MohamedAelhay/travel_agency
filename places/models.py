import os
from django.db import models

# Create your models here.
from django.utils.safestring import mark_safe


class Country(models.Model):
    country_Name = models.CharField(max_length=100)
    country_Pic = models.ImageField(upload_to='countries', max_length=250)

    def __str__(self):
        return self.country_Name

    def image_tag(self):
        return u'<img src="/media/%s" width=50 height=50/>' % self.country_Pic

    image_tag.short_description = 'Image'
    image_tag.allow_tags = True

    class Meta:
        verbose_name_plural = "Countries"


class City(models.Model):
    city_Name = models.CharField(max_length=100)
    city_Description = models.CharField(max_length=1000)
    city_Pic = models.ImageField(upload_to='cities', max_length=250)
    country_Name = models.ForeignKey(Country)

    def __str__(self):
        return self.city_Name

    def image_tag(self):
        return u'<img src="/media/%s" width=50 height=50/>' % self.city_Pic

    image_tag.short_description = 'Image'
    image_tag.allow_tags = True

    class Meta:
        verbose_name_plural = "Cities"


class Location(models.Model):
    loc_Name = models.CharField(max_length=100)
    loc_Description = models.CharField(max_length=1000, null=True, blank=True)
    loc_Pic = models.ImageField(upload_to='locations', max_length=250)
    city_Name = models.ForeignKey(City)

    def __str__(self):
        return self.loc_Name

    def image_tag(self):
        return u'<img src="/media/%s" width=50 height=50/>' % self.loc_Pic

    image_tag.short_description = 'Image'
    image_tag.allow_tags = True


class Hotel(models.Model):
    hotel_Name = models.CharField(max_length=100)
    hotel_Pic = models.ImageField(upload_to='hotels', max_length=250)

    def __str__(self):
        return self.hotel_Name


class Room(models.Model):
    rooms = models.IntegerField(max_length=3)
    room_type = models.CharField(choices=[(1, "Single"), (2, "Double"), (3, "Triple")], max_length=2)
    hotel_Name = models.ForeignKey(Hotel)


class CityHotel(models.Model):
    city_id = models.ForeignKey(City)
    hotel_id = models.ForeignKey(Hotel)

    class Meta:
        verbose_name_plural = "Hotels"












