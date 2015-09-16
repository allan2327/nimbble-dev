from django.shortcuts import redirect
from django.contrib import messages
from braces.views import LoginRequiredMixin
from stravalib.client import Client
from django.views.generic import View
from nimbble.models import FitnessTracker, FitnessTrackerToken
from .signals import strava_activated


class TokenHandler(object):

    def add_fitness_token(self, user, code):
        sv_token = self.get_token_from_code(code)
        tracker = FitnessTracker.objects.get(name='strava')

        nimbble_token, added = FitnessTrackerToken.objects.get_or_create(user=user, tracker=tracker)

        nimbble_token.token = sv_token
        nimbble_token.save()

    def get_token_from_code(self, code):
        tracker = FitnessTracker.objects.get(name='strava')
        acct = tracker.account

        sv_token = Client().exchange_code_for_token(client_id=int(acct.app_id), client_secret=acct.app_secret, code=code)
        return sv_token


class StravaTokenRedirectView(LoginRequiredMixin, View):

    def get(self, request, *arg, **kwargs):
        try:
            user = request.user
            code = request.GET.get('code', '')

            TokenHandler().add_fitness_token(user, code)

            strava_activated.send(sender=request, nimbble_token=nimbble_token)
            messages.success(request, '{} Fitness tracker has been successfully activated.'.format('Strava'))
        except Exception:
            messages.error(request, '{} Fitness tracker was not successfully activated.'.format('Strava'))

        return redirect('ui:trackers')
