# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2019-02-17 22:49
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('places', '0019_auto_20190217_2055'),
    ]

    operations = [
        migrations.RenameField(
            model_name='userhotelreservation',
            old_name='res_Time',
            new_name='res_Date',
        ),
    ]
