# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('data', '0007_auto_20141118_1131'),
    ]

    operations = [
        migrations.AlterField(
            model_name='incident',
            name='location_occurred',
            field=models.ForeignKey(to='data.Location', null=True),
        ),
    ]
