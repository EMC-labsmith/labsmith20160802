# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('device_management', '0062_auto_20160628_1651'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='device',
            name='Location',
        ),
        migrations.AddField(
            model_name='device',
            name='Device_location',
            field=models.CharField(blank=True, max_length=20, null=True, choices=[(b'Rack1', b'Rack1'), (b'Rack2', b'Rack2'), (b'Rack3', b'Rack3'), (b'Rack4', b'Rack4')]),
            preserve_default=True,
        ),
    ]
