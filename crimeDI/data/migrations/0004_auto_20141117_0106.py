# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('data', '0003_auto_20141116_2111'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='property',
            name='loss',
        ),
        migrations.RemoveField(
            model_name='property',
            name='thing',
        ),
        migrations.AddField(
            model_name='property',
            name='action',
            field=models.CharField(max_length=20, null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='property',
            name='num_thing',
            field=models.CharField(max_length=50, null=True),
            preserve_default=True,
        ),
    ]
