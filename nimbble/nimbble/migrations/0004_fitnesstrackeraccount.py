# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('nimbble', '0003_auto_20150825_2007'),
    ]

    operations = [
        migrations.CreateModel(
            name='FitnessTrackerAccount',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', auto_created=True, primary_key=True)),
                ('app_id', models.CharField(max_length=32)),
                ('app_secret', models.CharField(max_length=64)),
                ('tracker', models.OneToOneField(to='nimbble.FitnessTracker', related_name='account')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
