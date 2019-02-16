# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2019-02-15 22:53
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('places', '0007_auto_20190215_2253'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment_Text', models.CharField(max_length=500)),
                ('comment_Created_at', models.DateTimeField(auto_now_add=True)),
                ('comment_Updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name_plural': 'Comments',
            },
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('post_Text', models.CharField(max_length=500)),
                ('post_Created_at', models.DateTimeField(auto_now_add=True)),
                ('post_Updated_at', models.DateTimeField(auto_now=True)),
                ('city_Name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='places.City')),
                ('user_Name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'Posts',
            },
        ),
        migrations.AddField(
            model_name='comment',
            name='post_Id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog.Post'),
        ),
        migrations.AddField(
            model_name='comment',
            name='user_Name',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
