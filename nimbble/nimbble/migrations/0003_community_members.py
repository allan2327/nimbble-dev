# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('nimbble', '0002_auto_20150819_2141'),
    ]

    operations = [
        migrations.AddField(
            model_name='community',
            name='members',
            field=models.ManyToManyField(related_name='communities', to=settings.AUTH_USER_MODEL),
            preserve_default=True,
        ),
    ]
