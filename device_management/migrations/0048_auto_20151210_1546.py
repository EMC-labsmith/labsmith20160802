# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('device_management', '0047_auto_20151210_1544'),
    ]

    operations = [
        migrations.RenameField(
            model_name='slicsfpinfo',
            old_name='reservenumber',
            new_name='reserve_number',
        ),
        migrations.RenameField(
            model_name='slicsfpinfo',
            old_name='timestamp',
            new_name='time',
        ),
    ]
