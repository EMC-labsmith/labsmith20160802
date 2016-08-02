# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('device_management', '0036_auto_20151127_1728'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='npedevice',
            name='owner',
        ),
        migrations.RemoveField(
            model_name='npedevice',
            name='wanted',
        ),
        migrations.DeleteModel(
            name='NPEDevice',
        ),
        migrations.RemoveField(
            model_name='switchport',
            name='owner',
        ),
        migrations.DeleteModel(
            name='SwitchPort',
        ),
        migrations.AddField(
            model_name='device',
            name='comment',
            field=models.CharField(max_length=1000, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='device',
            name='cs0_ip',
            field=models.CharField(max_length=17, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='device',
            name='cs1_ip',
            field=models.CharField(max_length=17, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='device',
            name='drive_1225',
            field=models.CharField(max_length=30, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='device',
            name='dvt_evt',
            field=models.CharField(max_length=30, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='device',
            name='hostpc_ip',
            field=models.CharField(max_length=17, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='device',
            name='model',
            field=models.CharField(max_length=300, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='device',
            name='status',
            field=models.CharField(max_length=300, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='device',
            name='link',
            field=models.URLField(max_length=30, null=True, blank=True),
            preserve_default=True,
        ),
    ]
