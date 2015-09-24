# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Community',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, primary_key=True, verbose_name='ID')),
                ('name', models.CharField(unique=True, max_length=100)),
                ('city', models.CharField(max_length=100, blank=True, default='')),
                ('state', models.CharField(max_length=100, blank=True, default='')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('is_default', models.BooleanField(default=False)),
                ('members', models.ManyToManyField(to=settings.AUTH_USER_MODEL, related_name='communities')),
            ],
            options={
                'ordering': ('created',),
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='CommunityActivityLink',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, primary_key=True, verbose_name='ID')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='FitnessActivity',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, primary_key=True, verbose_name='ID')),
                ('source_id', models.IntegerField()),
                ('source_name', models.CharField(max_length=100)),
                ('activity_type', models.CharField(max_length=100)),
                ('average_watts', models.DecimalField(max_digits=6, decimal_places=2)),
                ('distance', models.DecimalField(max_digits=7, decimal_places=2)),
                ('moving_time', models.IntegerField()),
                ('score', models.IntegerField(default=0)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('user', models.ForeignKey(related_name='activities', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ('activity_type', 'source_id'),
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='FitnessTracker',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, primary_key=True, verbose_name='ID')),
                ('name', models.CharField(unique=True, max_length=100)),
                ('description', models.TextField()),
                ('icon_url', models.CharField(max_length=150)),
                ('tracker_link', models.URLField(max_length=150)),
                ('auth_url', models.URLField(max_length=512)),
                ('created', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'ordering': ('name',),
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='FitnessTrackerAccount',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, primary_key=True, verbose_name='ID')),
                ('app_id', models.CharField(max_length=32)),
                ('app_secret', models.CharField(max_length=64)),
                ('tracker', models.OneToOneField(related_name='account', to='nimbble.FitnessTracker')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='FitnessTrackerToken',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, primary_key=True, verbose_name='ID')),
                ('token', models.CharField(max_length=256)),
                ('tracker', models.ForeignKey(related_name='tokens', to='nimbble.FitnessTracker')),
                ('user', models.ForeignKey(related_name='tokens', to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AlterUniqueTogether(
            name='fitnesstrackertoken',
            unique_together=set([('user', 'tracker')]),
        ),
        migrations.AlterUniqueTogether(
            name='fitnessactivity',
            unique_together=set([('user', 'source_name', 'source_id')]),
        ),
        migrations.AddField(
            model_name='communityactivitylink',
            name='activity',
            field=models.OneToOneField(related_name='community_link', to='nimbble.FitnessActivity'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='communityactivitylink',
            name='community',
            field=models.ForeignKey(related_name='activity_links', to='nimbble.Community'),
            preserve_default=True,
        ),
    ]
