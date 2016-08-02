# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('device_management', '0046_auto_20151210_1527'),
    ]

    operations = [
        migrations.RenameField(
            model_name='slicsfpinfo',
            old_name='number',
            new_name='reservenumber',
        ),
    ]
