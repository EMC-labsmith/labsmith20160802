# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('device_management', '0025_npedevice_dvt_evt'),
    ]

    operations = [
        migrations.AddField(
            model_name='npedevice',
            name='drive_1225',
            field=models.CharField(max_length=30, null=True, blank=True),
            preserve_default=True,
        ),
    ]
