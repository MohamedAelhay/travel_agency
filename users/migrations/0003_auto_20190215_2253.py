# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2019-02-15 22:53
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_auto_20190214_2114'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='avatar',
            field=models.ImageField(upload_to='static/avatar/'),
        ),
    ]