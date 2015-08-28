# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('nimbble', '0002_community_is_default'),
    ]

    operations = [
        migrations.CreateModel(
            name='FitnessTrackerToken',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, primary_key=True, serialize=False)),
                ('token', models.CharField(max_length=256)),
                ('tracker', models.ForeignKey(to='nimbble.FitnessTracker', related_name='tokens')),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL, related_name='tokens')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AlterUniqueTogether(
            name='authtracker',
            unique_together=None,
        ),
        migrations.RemoveField(
            model_name='authtracker',
            name='tracker',
        ),
        migrations.RemoveField(
            model_name='authtracker',
            name='user',
        ),
        migrations.DeleteModel(
            name='AuthTracker',
        ),
        migrations.AlterUniqueTogether(
            name='fitnesstrackertoken',
            unique_together=set([('user', 'tracker')]),
        ),
    ]
