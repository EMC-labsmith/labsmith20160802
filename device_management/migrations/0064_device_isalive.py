# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('device_management', '0063_auto_20160630_1707'),
    ]

    operations = [
        migrations.AddField(
            model_name='device',
            name='isalive',
            field=models.BooleanField(default=True),
            preserve_default=True,
        ),
    ]
