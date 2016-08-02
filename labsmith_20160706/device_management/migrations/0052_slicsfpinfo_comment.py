# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('device_management', '0051_remove_slicsfpinfo_available_number'),
    ]

    operations = [
        migrations.AddField(
            model_name='slicsfpinfo',
            name='comment',
            field=models.CharField(max_length=1000, null=True, blank=True),
            preserve_default=True,
        ),
    ]
