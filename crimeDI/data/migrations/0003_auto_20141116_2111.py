# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('data', '0002_auto_20141113_2318'),
    ]

    operations = [
        migrations.CreateModel(
            name='Agency',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=30)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Arrest',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('datetime', models.DateTimeField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Arrestee',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=100)),
                ('age', models.IntegerField(default=0)),
                ('sex', models.CharField(max_length=1, null=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Incident',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('code', models.CharField(max_length=20)),
                ('datetime_occurred', models.DateTimeField(null=True)),
                ('datetime_reported', models.DateTimeField(null=True)),
                ('summary', models.TextField()),
                ('raw_entry', models.TextField(null=True)),
                ('agency', models.ForeignKey(to='data.Agency')),
                ('arrests', models.ManyToManyField(to='data.Arrest', null=True)),
                ('crimes', models.ManyToManyField(to='data.Crime')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=50, null=True, blank=True)),
                ('address', models.CharField(max_length=100, null=True)),
                ('latitude', models.FloatField(max_length=100, null=True)),
                ('longitude', models.FloatField(max_length=100, null=True)),
                ('intersection', models.BooleanField(default=False)),
                ('block', models.BooleanField(default=False)),
                ('city', models.CharField(max_length=70, null=True, blank=True)),
                ('agency', models.ForeignKey(to='data.Agency')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Offender',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=50)),
                ('description', models.CharField(max_length=255)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Officer',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=50)),
                ('badge_num', models.IntegerField(null=True)),
                ('agency', models.ForeignKey(to='data.Agency')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Property',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('loss', models.CharField(max_length=15)),
                ('thing', models.CharField(max_length=50)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Race',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=10)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Victim',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('age', models.IntegerField(default=0)),
                ('sex', models.CharField(max_length=1, null=True)),
                ('name', models.CharField(max_length=50, null=True)),
                ('origin', models.CharField(max_length=50, null=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='offender',
            name='race',
            field=models.ForeignKey(to='data.Race'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='incident',
            name='location_occurred',
            field=models.ForeignKey(to='data.Location'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='incident',
            name='offenders',
            field=models.ManyToManyField(to='data.Offender', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='incident',
            name='officer',
            field=models.ForeignKey(to='data.Officer'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='incident',
            name='properties',
            field=models.ManyToManyField(to='data.Property', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='arrestee',
            name='address',
            field=models.ForeignKey(to='data.Location'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='arrestee',
            name='race',
            field=models.ForeignKey(to='data.Race'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='arrest',
            name='arrestee',
            field=models.ForeignKey(to='data.Arrestee'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='arrest',
            name='charges',
            field=models.ForeignKey(to='data.Crime'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='arrest',
            name='location',
            field=models.ForeignKey(to='data.Location'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='arrest',
            name='officer',
            field=models.ForeignKey(to='data.Officer'),
            preserve_default=True,
        ),
        migrations.RemoveField(
            model_name='crime',
            name='address',
        ),
        migrations.RemoveField(
            model_name='crime',
            name='attempt',
        ),
        migrations.RemoveField(
            model_name='crime',
            name='date_time',
        ),
        migrations.RemoveField(
            model_name='crime',
            name='incident',
        ),
        migrations.RemoveField(
            model_name='crime',
            name='incident_num',
        ),
        migrations.RemoveField(
            model_name='crime',
            name='location_name',
        ),
        migrations.RemoveField(
            model_name='crime',
            name='officer',
        ),
        migrations.RemoveField(
            model_name='crime',
            name='summary',
        ),
        migrations.AddField(
            model_name='crime',
            name='arrests',
            field=models.IntegerField(default=0),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='crime',
            name='code',
            field=models.CharField(max_length=255, null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='crime',
            name='description',
            field=models.TextField(max_length=255, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='crime',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, default=0, serialize=False, verbose_name='ID'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='crime',
            name='name',
            field=models.CharField(default='Boo', max_length=255),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='crime',
            name='total_count',
            field=models.IntegerField(default=0),
            preserve_default=True,
        ),
    ]
