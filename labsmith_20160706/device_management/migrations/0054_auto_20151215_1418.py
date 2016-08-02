# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('device_management', '0053_auto_20151215_1404'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='slicsfp',
            name='info',
        ),
        migrations.AddField(
            model_name='slicsfpinfo',
            name='info',
            field=models.CharField(max_length=1000, null=True, blank=True),
            preserve_default=True,
        ),
    ]
