# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('device_management', '0049_slicsfpinfo_release_number'),
    ]

    operations = [
        migrations.AddField(
            model_name='slicsfpinfo',
            name='available_number',
            field=models.CharField(max_length=30, null=True, blank=True),
            preserve_default=True,
        ),
    ]
