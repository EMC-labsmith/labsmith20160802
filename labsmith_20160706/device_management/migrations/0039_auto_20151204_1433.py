# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('device_management', '0038_device_lock'),
    ]

    operations = [
        migrations.AlterField(
            model_name='device',
            name='link',
            field=models.URLField(max_length=1000, null=True, blank=True),
            preserve_default=True,
        ),
    ]
