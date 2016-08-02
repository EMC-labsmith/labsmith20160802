# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('device_management', '0022_auto_20151125_1600'),
    ]

    operations = [
        migrations.RenameField(
            model_name='npedevice',
            old_name='info',
            new_name='comment',
        ),
        migrations.RenameField(
            model_name='npedevice',
            old_name='spa_mac',
            new_name='cs0_ip',
        ),
        migrations.RenameField(
            model_name='npedevice',
            old_name='spb_mac',
            new_name='cs1_ip',
        ),
        migrations.RenameField(
            model_name='npedevice',
            old_name='pxeFilePath',
            new_name='model',
        ),
        migrations.RemoveField(
            model_name='npedevice',
            name='link',
        ),
        migrations.AddField(
            model_name='npedevice',
            name='hostpc_ip',
            field=models.CharField(max_length=17, null=True, blank=True),
            preserve_default=True,
        ),
    ]
