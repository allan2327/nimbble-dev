# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('nimbble', '0003_community_members'),
    ]

    operations = [
        migrations.CreateModel(
            name='AuthTracker',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, primary_key=True, serialize=False)),
                ('token', models.CharField(max_length=256)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='FitnessTracker',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, primary_key=True, serialize=False)),
                ('name', models.CharField(unique=True, max_length=100)),
                ('description', models.TextField()),
                ('icon_url', models.CharField(max_length=100)),
                ('tracker_link', models.URLField(max_length=100)),
                ('auth_url', models.URLField(max_length=512)),
                ('created', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'ordering': ('name',),
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='authtracker',
            name='tracker',
            field=models.ForeignKey(to='nimbble.FitnessTracker', related_name='authentications'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='authtracker',
            name='user',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL, related_name='trackers'),
            preserve_default=True,
        ),
        migrations.AlterUniqueTogether(
            name='authtracker',
            unique_together=set([('user', 'tracker')]),
        ),
    ]
