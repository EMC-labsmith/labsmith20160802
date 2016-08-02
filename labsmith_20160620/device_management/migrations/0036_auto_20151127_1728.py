# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('device_management', '0035_switchport_info'),
    ]

    operations = [
        migrations.RenameField(
            model_name='switchport',
            old_name='info',
            new_name='port',
        ),
        migrations.RemoveField(
            model_name='switchport',
            name='wanted',
        ),
    ]
