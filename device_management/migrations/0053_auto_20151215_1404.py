# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('device_management', '0052_slicsfpinfo_comment'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='slicsfpinfo',
            name='comment',
        ),
        migrations.AddField(
            model_name='slicsfp',
            name='info',
            field=models.CharField(max_length=1000, null=True, blank=True),
            preserve_default=True,
        ),
    ]
