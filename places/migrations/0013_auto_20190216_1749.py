# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2019-02-16 17:49
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('places', '0012_auto_20190216_1724'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='usercityrate',
            unique_together=set([]),
        ),
    ]
