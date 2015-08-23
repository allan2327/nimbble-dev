# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_remove_user_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='points',
            field=models.FloatField(default=0),
        ),
    ]
