# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('device_management', '0063_auto_20160606_1904'),
    ]

    operations = [
        migrations.AlterField(
            model_name='device',
            name='user',
            field=models.CharField(max_length=70, null=True, blank=True),
            preserve_default=True,
        ),
    ]
