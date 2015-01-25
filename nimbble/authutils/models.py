# -*- coding: utf-8 -*-

# Import the basic Django ORM models library
from django.db import models


# Subclass AbstractUser
class AuthorizedEmail(models.Model):

    email_postfix = models.CharField(max_length=128)

    def __unicode__(self):
        return self.username
