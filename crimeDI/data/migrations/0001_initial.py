# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Crime',
            fields=[
                ('incident_num', models.CharField(max_length=10, serialize=False, primary_key=True)),
                ('incident', models.CharField(max_length=20, null=True, blank=True)),
                ('attempt', models.BooleanField(default=False)),
                ('location', models.CharField(max_length=80)),
                ('location_name', models.CharField(max_length=50, null=True, blank=True)),
                ('officer', models.CharField(max_length=30)),
                ('date_time', models.DateTimeField(null=True, blank=True)),
                ('summary', models.CharField(max_length=200)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
