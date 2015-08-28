from django.test import TestCase
from django.contrib.sites.models import Site
from unittest.mock import patch, MagicMock
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
    def test_post_add_correctly_sets_auth_url(self, mock_reverse):
        curr_site = Site.objects.create(domain='test.com', name='testsite')

        with self.settings(SITE_ID=curr_site.id):
            mock_reverse.return_value = 'reverse auth url'
            StravaConfig().post_add('', '')
            mock_reverse.assert_called_with('ui:tracker_auth', {'tracker_name': 'strava'})

















def next():
    pass
