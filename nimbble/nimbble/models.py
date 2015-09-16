from django.db import models
from users.models import User

# Create your models here.

class Community(models.Model):

    name = models.CharField(max_length=100, blank=False, unique=True)
    city = models.CharField(max_length=100, blank=True, default='')
    state = models.CharField(max_length=100, blank=True, default='')
    created = models.DateTimeField(auto_now_add=True)
    members = models.ManyToManyField(User, related_name="communities")
    is_default = models.BooleanField(default=False)

    class Meta:
        ordering = ('created',)

    def __str__(self):
        return self.name

class FitnessTracker(models.Model):
    name = models.CharField(max_length=100, blank=False, unique=True)
    description = models.TextField()
    icon_url = models.CharField(max_length=150)
    tracker_link = models.URLField(max_length=150)
    auth_url = models.URLField(max_length=512)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering=('name',)

    def __str__(self):
        return self.name


class FitnessTrackerAccount(models.Model):
    tracker = models.OneToOneField(FitnessTracker, related_name='account')
    app_id = models.CharField(max_length=32, blank=False)
    app_secret = models.CharField(max_length=64, blank=False)

    def __str__(self):
        return '{} Account'.format(self.tracker.name)


class FitnessTrackerToken(models.Model):
    user = models.ForeignKey(User, related_name='tokens')
    tracker = models.ForeignKey(FitnessTracker, related_name='tokens')
    token = models.CharField(max_length=256, blank=False)

    class Meta:
        unique_together = ('user', 'tracker',)

    def __str__(self):
        return 'Token for {}:{}'.format(self.tracker.name, self.user.username)
