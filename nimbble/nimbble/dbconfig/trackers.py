from nimbble.models import FitnessTracker, FitnessTrackerAccount
from stravalib.client import Client
from django.contrib.sites.models import Site
from django.core.urlresolvers import reverse

class TrackerConfigFactory:
    factories = {}

    @classmethod
    def create(cls, name):
        if name not in TrackerConfigFactory.factories:
            config_name = '{}Config.Factory()'.format(name.title())
            TrackerConfigFactory.factories[name] = eval(config_name)

        return TrackerConfigFactory.factories[name].create()


class StravaConfig(object):
    def post_add(self, tracker, acct):
        current_site = Site.objects.get_current()
        redirect_url = '{}{}'.format(current_site.domain, reverse('ui:tracker_auth', {'tracker_name': 'strava'}))
        #tracker.auth_url = Client().authorization_url(client_id=acc.client_id, redirect_uri=redirect_url)
        #tracker.save()

    class Factory:
        def create(self): return StravaConfig()


class CustomFitnessTrackerMigration(object):

    def add_tracker(name, tracker_obj):
        tracker = FitnessTracker.objects.get_or_create(tracker_obj['info'])
        tracker_acct = FitnessTrackerAccount.objects.get_or_create(tracker_info['account'])

        TrackerConfigFactory().create(name).post_add(tracker, tracker_acct)
