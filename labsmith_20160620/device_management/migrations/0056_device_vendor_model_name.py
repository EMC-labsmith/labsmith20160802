# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('device_management', '0055_auto_20151216_1534'),
    ]

    operations = [
        migrations.AddField(
            model_name='device',
            name='vendor_model_name',
            field=models.CharField(max_length=30, null=True, blank=True),
            preserve_default=True,
        ),
    ]
