from django.test import TestCase
from django.http import HttpRequest
from unittest.mock import patch, MagicMock

from nimbble.models import FitnessTracker, FitnessTrackerAccount, FitnessTrackerToken
from users.models import User

from .views import TokenHandler, StravaTokenRedirectView
from .receivers import sync_user_activities
# Create your tests here.


class TestTokenHanlder(TestCase):

    def setUp(self):
        self.tracker = FitnessTracker.objects.create(name='strava')
        self.account = FitnessTrackerAccount.objects.create(tracker=self.tracker, app_id='4123', app_secret='my app secret')
        self.user = User.objects.create(username='tuser12')


    @patch('nimbble.fitnessaccount.strava.views.Client.exchange_code_for_token')
    def test_get_token_given_code(self, mock_code_exchange):
        code = 'code given by strava'
        expected_token = 'new token'
        handler = TokenHandler()

        mock_code_exchange.return_value = expected_token
        token = handler.get_token_from_code(code)

        self.assertEquals(token, expected_token)


    @patch('nimbble.fitnessaccount.strava.views.Client.exchange_code_for_token')
    def test_get_token_passes_correct_parameters(self, mock_code_exchange):
        code = 'code given by strava'
        handler = TokenHandler()

        mock_code_exchange.return_value = 'token'
        token = handler.get_token_from_code(code)

        mock_code_exchange.assert_called_with(code=code,
                                              client_id=int(self.account.app_id),
                                              client_secret=self.account.app_secret)

    def test_add_fitness_tracker(self):
        code = 'code given by strava'
        handler = TokenHandler()
        handler.get_token_from_code = MagicMock()
        handler.get_token_from_code.return_value = 'my token'

        handler.add_fitness_token(self.user, code)

        new_token = FitnessTrackerToken.objects.get(token='my token')
        self.assertEquals(new_token.user, self.user)
        self.assertEquals(new_token.tracker, self.tracker)


class TestStravaTokenRedirectView(TestCase):

    def setUp(self):
        self.user = User.objects.create(username='testuser')
        self.tracker = FitnessTracker.objects.create(name='strava')

        self.request = HttpRequest()
        self.request.user = self.user
        self.request.GET = { 'code': 'my strava code' }


    @patch('nimbble.fitnessaccount.strava.views.redirect')
    @patch('nimbble.fitnessaccount.strava.views.messages')
    @patch('nimbble.fitnessaccount.strava.views.strava_activated')
    @patch('nimbble.fitnessaccount.strava.views.TokenHandler.add_fitness_token')
    def test_get_adds_fitness_tracker(self, mock_token_handler, *args):

        StravaTokenRedirectView().get(self.request)
        mock_token_handler.assert_called_with(self.user, self.request.GET.get('code'))



from datetime import datetime, timedelta
class TestSyncUserActivitiesReceiver(TestCase):


    def setUp(self):
        self.user = User.objects.create(username='testuser')
        self.tracker = FitnessTracker.objects.create(name='strava')


    @patch('nimbble.fitnessaccount.strava.receivers.StravaDataGatherer.sync')
    def test_receiver_calls_data_gatherer_with_token(self, mock_sync_handler):
        token = FitnessTrackerToken.objects.create(user=self.user, tracker=self.tracker, token='sample token')
        sync_user_activities(None, self.user)
        mock_sync_handler.assert_called_with(user=self.user, token=token)


    @patch('nimbble.fitnessaccount.strava.receivers.StravaDataGatherer.sync')
    def test_receiver_calls_data_gatherer_without_token(self, mock_sync_handler):
        sync_user_activities(None, self.user)
        self.assertFalse(mock_sync_handler.called)









def asdf():
    pass
