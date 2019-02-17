import os

from django.db import models
from users.models import CustomUser
from datetime import datetime    

# Create your models here.
from django.utils.safestring import mark_safe


class Country(models.Model):
    country_Name = models.CharField(max_length=100)
    country_Pic = models.ImageField(upload_to='static/countries/', max_length=250)

    def __str__(self):
        return self.country_Name

    class Meta:
        verbose_name_plural = "Countries"


class City(models.Model):
    city_Name = models.CharField(max_length=100)
    city_Description = models.CharField(max_length=1000)
    city_Pic = models.ImageField(upload_to='static/cities/', max_length=250)
    country_Name = models.ForeignKey(Country)

    def __str__(self):
        return self.city_Name

    def url(self):
        return os.path.join('/static/cities', os.path.basename(str(self.city_Pic)))

    def image_tag(self):
        # return mark_safe('<img src="{}" width="150" height="150" />'.format(self.url()))
        return u'<img src="%s" width=50 height=50/>' % self.city_Pic
        # return mark_safe('<img src="%s" width="150" height="150" />' % self.city_Pic)

    image_tag.short_description = 'Image'
    image_tag.allow_tags = True

    class Meta:
        verbose_name_plural = "Cities"


class Location(models.Model):
    loc_Name = models.CharField(max_length=100)
    loc_Description = models.CharField(max_length=1000, null=True, blank=True)
    loc_Pic = models.ImageField(upload_to='static/locations/', max_length=250)
    city_Name = models.ForeignKey(City)

    def __str__(self):
        return self.loc_Name


class Hotel(models.Model):
    hotel_Name = models.CharField(max_length=100)
    hotel_Pic = models.ImageField(upload_to='static/hotels/', max_length=250)

    def __str__(self):
        return self.hotel_Name


class CityHotel(models.Model):
    city_id = models.ForeignKey(City)
    hotel_id = models.ForeignKey(Hotel)

    class Meta:
        verbose_name_plural = "Hotels"

class UserCityRate(models.Model):
    user = models.ForeignKey(CustomUser)
    city = models.ForeignKey(City)
    rate    = models.IntegerField(
        default = 3,
        choices = (
            (1, 'Bad'),
            (2, 'Below Average'),
            (3, 'Average'),
            (4, 'Very Good'),
            (5, 'Excelent'),
        )
    )

    class Meta:
        unique_together = (('user', 'city'),)
    
    def __str__(self):
        return self.rate

class UserCarRent(models.Model):
    pickup_loc   = models.ForeignKey(Location, related_name = 'pickup_loc')
    dropoff_loc  = models.ForeignKey(Location, related_name = 'dropoff_loc')
    user     = models.ForeignKey(CustomUser)
    time     = models.DateTimeField(default = datetime.now)
    
    def __str__(self):
        return self.time












