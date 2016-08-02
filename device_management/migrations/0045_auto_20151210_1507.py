# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('device_management', '0044_slicsfpinfo'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='slicsfpinfo',
            name='content',
        ),
        migrations.AddField(
            model_name='slicsfpinfo',
            name='number',
            field=models.CharField(max_length=30, null=True, blank=True),
            preserve_default=True,
        ),
    ]
