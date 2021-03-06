# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2019-02-17 20:55
from __future__ import unicode_literals

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('places', '0018_merge_20190217_1608'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserHotelReservation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rooms', models.IntegerField(max_length=3)),
                ('room_type', models.CharField(choices=[(1, 'Single'), (2, 'Double'), (3, 'Triple')], max_length=2)),
                ('res_Time', models.DateTimeField(default=datetime.datetime.now)),
            ],
        ),
        migrations.RemoveField(
            model_name='room',
            name='hotel_Name',
        ),
        migrations.AlterField(
            model_name='city',
            name='city_Pic',
            field=models.ImageField(max_length=250, upload_to='cities'),
        ),
        migrations.AlterField(
            model_name='country',
            name='country_Pic',
            field=models.ImageField(max_length=250, upload_to='countries'),
        ),
        migrations.AlterField(
            model_name='hotel',
            name='hotel_Pic',
            field=models.ImageField(max_length=250, upload_to='hotels'),
        ),
        migrations.AlterField(
            model_name='location',
            name='loc_Pic',
            field=models.ImageField(max_length=250, upload_to='locations'),
        ),
        migrations.DeleteModel(
            name='Room',
        ),
        migrations.AddField(
            model_name='userhotelreservation',
            name='hotel_Name',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='places.Hotel'),
        ),
        migrations.AddField(
            model_name='userhotelreservation',
            name='user_Name',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
