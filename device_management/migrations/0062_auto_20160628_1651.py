# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('device_management', '0061_device_port_ip'),
    ]

    operations = [
        migrations.AddField(
            model_name='device',
            name='Location',
            field=models.CharField(max_length=300, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='device',
            name='holdingTime',
            field=models.CharField(max_length=300, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='device',
            name='user',
            field=models.CharField(max_length=70, null=True, blank=True),
            preserve_default=True,
        ),
    ]
