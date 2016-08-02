# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('device_management', '0028_auto_20151126_1514'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='slicsfp',
            name='model',
        ),
        migrations.AddField(
            model_name='slicsfp',
            name='model_name',
            field=models.CharField(max_length=30, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='slicsfp',
            name='owner',
            field=models.ForeignKey(related_name='SlicSfp_owner_user', blank=True, to=settings.AUTH_USER_MODEL, null=True),
            preserve_default=True,
        ),
    ]
