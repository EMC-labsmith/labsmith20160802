# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('device_management', '0061_device_port_ip'),
    ]

    operations = [
        migrations.AddField(
            model_name='device',
            name='holdingTime',
            field=models.DateTimeField(default=datetime.datetime(2016, 6, 6, 9, 33, 9, 497000, tzinfo=utc)),
            preserve_default=False,
        ),
    ]
