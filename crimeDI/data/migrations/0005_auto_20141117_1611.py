# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('data', '0004_auto_20141117_0106'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='arrest',
            name='arrestee',
        ),
        migrations.RemoveField(
            model_name='arrest',
            name='charges',
        ),
        migrations.RemoveField(
            model_name='arrest',
            name='location',
        ),
        migrations.RemoveField(
            model_name='arrest',
            name='officer',
        ),
        migrations.RemoveField(
            model_name='arrestee',
            name='address',
        ),
        migrations.RemoveField(
            model_name='arrestee',
            name='race',
        ),
        migrations.DeleteModel(
            name='Arrestee',
        ),
        migrations.RemoveField(
            model_name='incident',
            name='agency',
        ),
        migrations.RemoveField(
            model_name='incident',
            name='arrests',
        ),
        migrations.DeleteModel(
            name='Arrest',
        ),
        migrations.RemoveField(
            model_name='incident',
            name='crimes',
        ),
        migrations.DeleteModel(
            name='Crime',
        ),
        migrations.RemoveField(
            model_name='incident',
            name='location_occurred',
        ),
        migrations.RemoveField(
            model_name='incident',
            name='offenders',
        ),
        migrations.RemoveField(
            model_name='incident',
            name='officer',
        ),
        migrations.RemoveField(
            model_name='incident',
            name='properties',
        ),
        migrations.DeleteModel(
            name='Incident',
        ),
        migrations.RemoveField(
            model_name='location',
            name='agency',
        ),
        migrations.DeleteModel(
            name='Location',
        ),
        migrations.RemoveField(
            model_name='offender',
            name='race',
        ),
        migrations.DeleteModel(
            name='Offender',
        ),
        migrations.RemoveField(
            model_name='officer',
            name='agency',
        ),
        migrations.DeleteModel(
            name='Agency',
        ),
        migrations.DeleteModel(
            name='Officer',
        ),
        migrations.DeleteModel(
            name='Property',
        ),
        migrations.DeleteModel(
            name='Race',
        ),
        migrations.DeleteModel(
            name='Victim',
        ),
    ]
