# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('device_management', '0023_auto_20151125_1605'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='npedevice',
            name='spa_term',
        ),
        migrations.RemoveField(
            model_name='npedevice',
            name='spb_term',
        ),
    ]
