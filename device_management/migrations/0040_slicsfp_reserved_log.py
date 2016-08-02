# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('device_management', '0039_auto_20151204_1433'),
    ]

    operations = [
        migrations.AddField(
            model_name='slicsfp',
            name='reserved_log',
            field=models.CharField(max_length=1000, null=True, blank=True),
            preserve_default=True,
        ),
    ]
