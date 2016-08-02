# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('device_management', '0050_slicsfpinfo_available_number'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='slicsfpinfo',
            name='available_number',
        ),
    ]
