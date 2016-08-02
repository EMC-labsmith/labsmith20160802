# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('device_management', '0032_switchport_port'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='switchport',
            name='port',
        ),
    ]
