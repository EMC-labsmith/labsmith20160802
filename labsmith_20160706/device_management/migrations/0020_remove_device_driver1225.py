# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('device_management', '0019_remove_device_dvt_evt'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='device',
            name='driver1225',
        ),
    ]
