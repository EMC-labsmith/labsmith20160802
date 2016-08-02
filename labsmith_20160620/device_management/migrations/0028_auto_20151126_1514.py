# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('device_management', '0027_slic_sfp_switch'),
    ]

    operations = [
        migrations.CreateModel(
            name='SLICSFP',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True)),
                ('user', models.CharField(max_length=20, null=True, blank=True)),
                ('model', models.CharField(max_length=300, null=True, blank=True)),
                ('PN', models.CharField(max_length=300, null=True, blank=True)),
                ('comment', models.CharField(max_length=1000, null=True, blank=True)),
                ('available_number', models.CharField(max_length=30, null=True, blank=True)),
                ('reserved_number', models.CharField(max_length=30, null=True, blank=True)),
                ('owner', models.ForeignKey(related_name='SLICSFP_owner_user', blank=True, to=settings.AUTH_USER_MODEL, null=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='SwitchPort',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True)),
                ('name', models.CharField(max_length=30)),
                ('user', models.CharField(max_length=20, null=True, blank=True)),
                ('owner', models.ForeignKey(related_name='SwitchPort_owner_user', blank=True, to=settings.AUTH_USER_MODEL, null=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.RemoveField(
            model_name='slic_sfp',
            name='owner',
        ),
        migrations.DeleteModel(
            name='SLIC_SFP',
        ),
        migrations.RemoveField(
            model_name='switch',
            name='owner',
        ),
        migrations.DeleteModel(
            name='SWITCH',
        ),
    ]
