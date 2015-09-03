from django.test import TestCase
from django.contrib.sites.models import Site
from unittest.mock import patch, MagicMock
from nimbble.models import FitnessTracker, FitnessTrackerAccount
from nimbble.dbconfig.trackers import TrackerConfigFactory, StravaConfig

class TrackerConfigFactoryTest(TestCase):

    def test_create_correctly_instanciates_strava(self):
        config_one = TrackerConfigFactory.create('strava')
        self.assertTrue(type(config_one) == StravaConfig)


class StravaConfigTest(TestCase):

    def test_factory_correctly_instaciates_config(self):
        new_tracker = StravaConfig.Factory().create()
        self.assertTrue(type(new_tracker) == StravaConfig)


    @patch('nimbble.dbconfig.trackers.reverse')
    @patch('nimbble.dbconfig.trackers.Client.authorization_url')
    def test_post_add_sets_tracker_auth_urll(self, mock_auth_url, mock_reverse):
        curr_site = Site.objects.create(domain='test.com', name='testsite')

        with self.settings(SITE_ID=curr_site.id):
            mock_reverse.return_value = 'reverse auth url'
            mock_auth_url.return_value = 'strava auth url'

            tracker = FitnessTracker()
            acc = FitnessTrackerAccount(app_id=123)

            StravaConfig().post_add(tracker, acc)

            self.assertEquals(mock_auth_url.return_value, tracker.auth_url)


    @patch('nimbble.dbconfig.trackers.reverse')
    @patch('nimbble.dbconfig.trackers.Client.authorization_url')
    def test_post_add_calls_reverse_with_correct_view_name(self, mock_auth_url, mock_reverse):
        curr_site = Site.objects.create(domain='test.com', name='testsite')

        with self.settings(SITE_ID=curr_site.id):
            mock_reverse.return_value = 'reverse auth url'
            mock_auth_url.return_value = 'strava auth url'

            tracker = FitnessTracker()
            acc = FitnessTrackerAccount(app_id=123)

            StravaConfig().post_add(tracker, acc)

            mock_reverse.assert_called_with('ui:tracker_auth', kwargs={'tracker_name': 'strava'})

    @patch('nimbble.dbconfig.trackers.reverse')
    @patch('nimbble.dbconfig.trackers.Client.authorization_url')
    def test_post_add_calls_client_with_correct_params(self, mock_auth_url, mock_reverse):
        curr_site = Site.objects.create(domain='test.com', name='testsite')

        with self.settings(SITE_ID=curr_site.id):
            mock_reverse.return_value = 'reverse auth url'
            mock_auth_url.return_value = 'strava auth url'

            tracker = FitnessTracker()
            acc = FitnessTrackerAccount(app_id=123)

            StravaConfig().post_add(tracker, acc)

            expected = '{}{}'.format(curr_site.domain, mock_reverse.return_value)
            mock_auth_url.assert_called_with(client_id=acc.app_id, redirect_uri=expected)

















def next():
    pass
