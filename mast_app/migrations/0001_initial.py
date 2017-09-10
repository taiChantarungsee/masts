# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2017-09-10 14:32
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CsvData',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('address1', models.CharField(max_length=30)),
                ('address2', models.CharField(max_length=30)),
                ('address3', models.CharField(max_length=30)),
                ('address4', models.CharField(max_length=30)),
                ('unit_name', models.CharField(max_length=30)),
                ('tenant_name', models.CharField(max_length=30)),
                ('lease_start_date', models.CharField(max_length=30, null=True)),
                ('lease_end_date', models.CharField(max_length=30, null=True)),
                ('lease_years', models.IntegerField(null=True)),
                ('current_rent', models.FloatField(null=True)),
            ],
        ),
    ]
