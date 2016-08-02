# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('device_management', '0045_auto_20151210_1507'),
    ]

    operations = [
        migrations.RenameField(
            model_name='slicsfp',
            old_name='available_number',
            new_name='total_number',
        ),
        migrations.RemoveField(
            model_name='slicsfp',
            name='history',
        ),
    ]
