# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('human', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='offender',
            name='location',
            field=models.CharField(default=None, max_length=30, blank=True),
        ),
        migrations.AlterField(
            model_name='offender',
            name='name',
            field=models.CharField(default=None, max_length=30, blank=True),
        ),
        migrations.AlterField(
            model_name='offender',
            name='person_image',
            field=models.ImageField(default=None, max_length=300, upload_to=b'', blank=True),
        ),
        migrations.AlterField(
            model_name='phone',
            name='latitude',
            field=models.FloatField(default=None, max_length=20, blank=True),
        ),
        migrations.AlterField(
            model_name='phone',
            name='location',
            field=models.CharField(default=None, max_length=30, blank=True),
        ),
        migrations.AlterField(
            model_name='phone',
            name='longitude',
            field=models.FloatField(default=None, max_length=20, blank=True),
        ),
    ]
