from nimbble.models import FitnessTracker, FitnessTrackerAccount
from stravalib.client import Client
from django.contrib.sites.models import Site
from django.core.urlresolvers import reverse
from nimbble.dbconfig.consts import TRACKERS

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
        redirect_url = '{}{}'.format(current_site.domain, reverse('strava_token_login'))
        tracker.auth_url = Client().authorization_url(client_id=acct.app_id, redirect_uri=redirect_url)
        tracker.save()

    class Factory:
        def create(self): return StravaConfig()


class CustomFitnessTrackerMigration(object):

    def import_tracker_info(self):
        for name in TRACKERS:
            print('importing {}'.format(name))
            self.add_tracker(name, TRACKERS[name])

        print('done importing')

    def add_tracker(self, name, tracker_obj):
        tracker,created = FitnessTracker.objects.get_or_create(name=name, defaults=tracker_obj['info'])
        tracker_acct,created = FitnessTrackerAccount.objects.get_or_create(app_id=tracker_obj['account']['app_id'], tracker=tracker)

        TrackerConfigFactory().create(name).post_add(tracker, tracker_acct)
