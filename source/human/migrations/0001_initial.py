# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Offender',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('phone_number', models.IntegerField()),
                ('name', models.CharField(max_length=30, null=True)),
                ('location', models.CharField(max_length=30, null=True)),
                ('person_image', models.ImageField(max_length=300, null=True, upload_to=b'')),
            ],
        ),
        migrations.CreateModel(
            name='Phone',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('phone_number', models.IntegerField()),
                ('area_code', models.IntegerField()),
                ('latitude', models.FloatField(max_length=20, null=True)),
                ('longitude', models.FloatField(max_length=20, null=True)),
                ('location', models.CharField(max_length=30, null=True)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
