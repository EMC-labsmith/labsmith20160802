# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('device_management', '0020_remove_device_driver1225'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='device',
            name='comment',
        ),
        migrations.RemoveField(
            model_name='device',
            name='cs0_ip',
        ),
        migrations.RemoveField(
            model_name='device',
            name='cs1_ip',
        ),
        migrations.RemoveField(
            model_name='device',
            name='hostpc_ip',
        ),
        migrations.RemoveField(
            model_name='device',
            name='model',
        ),
        migrations.AlterField(
            model_name='device',
            name='status',
            field=models.CharField(max_length=300, null=True, blank=True),
            preserve_default=True,
        ),
    ]
