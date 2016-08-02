# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('device_management', '0041_remove_slicsfp_reserved_log'),
    ]

    operations = [
        migrations.AlterField(
            model_name='device',
            name='lock',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
    ]
