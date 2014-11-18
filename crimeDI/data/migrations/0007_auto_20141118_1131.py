# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('data', '0006_auto_20141117_1612'),
    ]

    operations = [
        migrations.RenameField(
            model_name='location',
            old_name='address',
            new_name='address_name',
        ),
        migrations.RemoveField(
            model_name='incident',
            name='crimes',
        ),
        migrations.RemoveField(
            model_name='location',
            name='block',
        ),
        migrations.RemoveField(
            model_name='location',
            name='intersection',
        ),
        migrations.RemoveField(
            model_name='location',
            name='latitude',
        ),
        migrations.RemoveField(
            model_name='location',
            name='longitude',
        ),
        migrations.RemoveField(
            model_name='location',
            name='name',
        ),
        migrations.RemoveField(
            model_name='officer',
            name='badge_num',
        ),
    ]
