# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('device_management', '0033_remove_switchport_port'),
    ]

    operations = [
        migrations.AddField(
            model_name='switchport',
            name='wanted',
            field=models.ForeignKey(related_name='SwitchPort_wanted_user', blank=True, to=settings.AUTH_USER_MODEL, null=True),
            preserve_default=True,
        ),
    ]
