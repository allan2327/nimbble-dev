# -*- coding: utf-8 -*-
# Import the AbstractUser model
from django.contrib.auth.models import AbstractUser

# Import the basic Django ORM models library
from django.db import models

from django.utils.translation import ugettext_lazy as _


# Subclass AbstractUser
class User(AbstractUser):

    points = models.FloatField(default=0)
    picture_url = models.CharField(max_length=256)

    def __unicode__(self):
        return self.username
