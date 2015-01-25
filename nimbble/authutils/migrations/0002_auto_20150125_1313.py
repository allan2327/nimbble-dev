# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


def add_default_emails(apps, schema_editor):

    AuthorizedEmail = apps.get_model('authutils', 'AuthorizedEmail')

    postfixes = ['nimbble.com', 'test.com']

    for postfix in postfixes:
        e = AuthorizedEmail(email_postfix=postfix)
        e.save()



class Migration(migrations.Migration):

    dependencies = [
        ('authutils', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(add_default_emails)
    ]
