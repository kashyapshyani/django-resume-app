# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-07-26 17:48
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Resume',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
                ('photo', models.ImageField(blank=True, upload_to='photo')),
                ('address', models.CharField(max_length=200)),
                ('father', models.CharField(max_length=255)),
                ('mother', models.CharField(max_length=255)),
                ('email', models.EmailField(max_length=254)),
                ('cgpa', models.FloatField()),
                ('university', models.CharField(max_length=255)),
                ('certificate', models.CharField(blank=True, max_length=255)),
                ('skills', models.TextField()),
            ],
        ),
    ]
