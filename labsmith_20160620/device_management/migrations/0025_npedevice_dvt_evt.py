# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('device_management', '0024_auto_20151125_1607'),
    ]

    operations = [
        migrations.AddField(
            model_name='npedevice',
            name='dvt_evt',
            field=models.CharField(max_length=30, null=True, blank=True),
            preserve_default=True,
        ),
    ]
