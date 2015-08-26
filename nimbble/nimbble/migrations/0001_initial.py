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
            name='AuthTracker',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', primary_key=True, serialize=False)),
                ('token', models.CharField(max_length=256)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Community',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', primary_key=True, serialize=False)),
                ('name', models.CharField(unique=True, max_length=100)),
                ('city', models.CharField(blank=True, max_length=100, default='')),
                ('state', models.CharField(blank=True, max_length=100, default='')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('members', models.ManyToManyField(to=settings.AUTH_USER_MODEL, related_name='communities')),
            ],
            options={
                'ordering': ('created',),
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='FitnessTracker',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', primary_key=True, serialize=False)),
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
            field=models.ForeignKey(related_name='authentications', to='nimbble.FitnessTracker'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='authtracker',
            name='user',
            field=models.ForeignKey(related_name='trackers', to=settings.AUTH_USER_MODEL),
            preserve_default=True,
        ),
        migrations.AlterUniqueTogether(
            name='authtracker',
            unique_together=set([('user', 'tracker')]),
        ),
    ]
