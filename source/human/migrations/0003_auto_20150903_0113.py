# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('human', '0002_auto_20150903_0109'),
    ]

    operations = [
        migrations.AlterField(
            model_name='phone',
            name='latitude',
            field=models.FloatField(default=None, max_length=20, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='phone',
            name='location',
            field=models.CharField(default=None, max_length=30, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='phone',
            name='longitude',
            field=models.FloatField(default=None, max_length=20, null=True, blank=True),
        ),
    ]
