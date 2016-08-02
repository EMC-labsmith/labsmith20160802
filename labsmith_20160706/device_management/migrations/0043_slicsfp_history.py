# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('device_management', '0042_auto_20151209_1651'),
    ]

    operations = [
        migrations.AddField(
            model_name='slicsfp',
            name='history',
            field=models.CharField(max_length=1000, null=True, blank=True),
            preserve_default=True,
        ),
    ]
