# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('device_management', '0048_auto_20151210_1546'),
    ]

    operations = [
        migrations.AddField(
            model_name='slicsfpinfo',
            name='release_number',
            field=models.CharField(max_length=30, null=True, blank=True),
            preserve_default=True,
        ),
    ]
