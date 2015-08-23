from django.db import models
from users.models import User

# Create your models here.

class Community(models.Model):

    name = models.CharField(max_length=100, blank=False, unique=True)
    city = models.CharField(max_length=100, blank=True, default='')
    state = models.CharField(max_length=100, blank=True, default='')
    created = models.DateTimeField(auto_now_add=True)
    members = models.ManyToManyField(User, related_name="communities")

    class Meta:
        ordering = ('created',)

    def __str__(self):
        return self.name

class FitnessTracker(models.Model):
    name = models.CharField(max_length=100, blank=False, unique=True)
    description = models.TextField()
    icon_url = models.CharField(max_length=100)
    tracker_link = models.URLField(max_length=100)
    auth_url = models.URLField(max_length=512)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering=('name',)


class AuthTracker(models.Model):
    user = models.ForeignKey(User, related_name='trackers')
    tracker = models.ForeignKey(FitnessTracker, related_name='authentications')
    token = models.CharField(max_length=256, blank=False)

    class Meta:
        unique_together = ('user', 'tracker',)
