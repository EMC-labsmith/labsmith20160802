# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('device_management', '0043_slicsfp_history'),
    ]

    operations = [
        migrations.CreateModel(
            name='SlicSfpInfo',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True)),
                ('MachineName', models.CharField(max_length=30)),
                ('user', models.CharField(max_length=20, null=True, blank=True)),
                ('timestamp', models.DateTimeField()),
                ('content', models.CharField(max_length=1000, null=True, blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
