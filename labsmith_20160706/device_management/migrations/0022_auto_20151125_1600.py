# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('device_management', '0021_auto_20151125_1554'),
    ]

    operations = [
        migrations.CreateModel(
            name='NPEDevice',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True)),
                ('name', models.CharField(max_length=30)),
                ('link', models.URLField()),
                ('user', models.CharField(max_length=20, null=True, blank=True)),
                ('info', models.CharField(max_length=1000, null=True, blank=True)),
                ('spa_ip', models.CharField(max_length=20, null=True, blank=True)),
                ('spb_ip', models.CharField(max_length=20, null=True, blank=True)),
                ('spa_mac', models.CharField(max_length=17, null=True, blank=True)),
                ('spb_mac', models.CharField(max_length=17, null=True, blank=True)),
                ('mgmt_ip', models.CharField(max_length=20, null=True, blank=True)),
                ('spa_term', models.CharField(max_length=30, null=True, blank=True)),
                ('spb_term', models.CharField(max_length=30, null=True, blank=True)),
                ('bmc_spa_ip', models.CharField(max_length=20, null=True, blank=True)),
                ('bmc_spb_ip', models.CharField(max_length=20, null=True, blank=True)),
                ('platform_type', models.CharField(max_length=30, null=True, blank=True)),
                ('pxeFilePath', models.CharField(max_length=300, null=True, blank=True)),
                ('status', models.CharField(max_length=300, null=True, blank=True)),
                ('owner', models.ForeignKey(related_name='NPE_owner_user', blank=True, to=settings.AUTH_USER_MODEL, null=True)),
                ('wanted', models.ForeignKey(related_name='NPE_wanted_user', blank=True, to=settings.AUTH_USER_MODEL, null=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.RemoveField(
            model_name='device',
            name='status',
        ),
    ]
