# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2019-02-16 19:55
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('places', '0016_auto_20190216_1953'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='UserCarRent2',
            new_name='UserCarRent',
        ),
    ]
