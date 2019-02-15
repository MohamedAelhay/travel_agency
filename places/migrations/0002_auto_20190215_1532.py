# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2019-02-15 15:32
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('places', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='city',
            old_name='name',
            new_name='city_name',
        ),
        migrations.RenameField(
            model_name='city',
            old_name='pic',
            new_name='city_pic',
        ),
        migrations.RenameField(
            model_name='country',
            old_name='name',
            new_name='country_Name',
        ),
        migrations.RenameField(
            model_name='country',
            old_name='pic',
            new_name='country_Pic',
        ),
        migrations.RenameField(
            model_name='hotel',
            old_name='name',
            new_name='hotel_name',
        ),
        migrations.RenameField(
            model_name='hotel',
            old_name='pic',
            new_name='hotel_pic',
        ),
        migrations.RenameField(
            model_name='location',
            old_name='name',
            new_name='loc_name',
        ),
        migrations.RenameField(
            model_name='location',
            old_name='pic',
            new_name='loc_pic',
        ),
    ]
