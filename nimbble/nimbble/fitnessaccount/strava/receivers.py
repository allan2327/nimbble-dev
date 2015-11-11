from django.dispatch import receiver
from .signals import strava_activated
from stravalib.client import Client
from datetime import datetime, timedelta
from nimbble.models import FitnessActivity, CommunityActivityLink, FitnessTracker, FitnessTrackerToken
from nimbble.fitnessaccount.signals import activities_loaded
from nimbble.signals import sync_activities
import math

class QuadraticPointCalculator(object):

    COEFFICIENT = {
        'ride': 0.05,         # y = sqrt([(5)^2/500)]*x)
        'run': 0.2,           # y = sqrt([(10]^2/500]*x)
        'swim': 0.2,
    }

    def update_score(self, activity):
        scale = self.COEFFICIENT.get(activity.activity_type.lower(), 0.01)
        score = math.sqrt(float(scale) * float(activity.average_watts + activity.distance))
        activity.score = score


class StravaActivityConverter(object):
    METER_TO_MILE = 0.000621371

    def __init__(self, calculator):
        self.calculator = calculator

    def create_activity(self, user, strava_act):
        distance = strava_act.distance.num * self.METER_TO_MILE
        new_activity, created = FitnessActivity.objects.get_or_create(
            user = user,
            source_name = 'strava',
            source_id = strava_act.id,
            defaults={
                'activity_type': strava_act.type,
                'average_watts': strava_act.average_watts if strava_act.average_watts else 5,
                'distance': round(distance, 2),
                'moving_time': strava_act.moving_time.total_seconds(),
                'start_date': strava_act.start_date
            },
        )

        self.calculator.update_score(new_activity)
        new_activity.save()

        default_comm = user.communities.get(is_default=True)
        CommunityActivityLink.objects.get_or_create(community=default_comm, activity=new_activity)


class StravaDataGatherer(object):

    def set_picture(self, user, nimbble_token):
        if len(user.picture_url) != 0 and '128.png' not in user.picture_url:
            return

        client = Client(access_token=nimbble_token.token)
        athlete = client.get_athlete()

        user.picture_url = athlete.profile_medium
        user.save()


    def sync(self, user, token, **kwargs):
        client = Client(access_token=token)
        days = kwargs['days'] if 'days' in kwargs else 10
        after = datetime.today() - timedelta(days=days)

        activities = client.get_activities(after=after)

        converter = StravaActivityConverter(QuadraticPointCalculator())
        for strava_act in activities:
            converter.create_activity(user, strava_act)



@receiver(strava_activated)
def update_user_picture(sender, nimbble_token, **kwargs):
    user = nimbble_token.user
    StravaDataGatherer().set_picture(user, nimbble_token)


@receiver(strava_activated)
def update_user_activities(sender, nimbble_token, **kwargs):
    StravaDataGatherer().sync(user=nimbble_token.user, token=nimbble_token.token, days=60)
    activities_loaded.send(sender=sender, user=nimbble_token.user)


from django.core.exceptions import ObjectDoesNotExist
from requests.exceptions import HTTPError
from django.contrib import messages

@receiver(sync_activities)
def sync_user_activities(sender, user, **kwargs):
    tracker = FitnessTracker.objects.get(name='strava')

    try:
        token = FitnessTrackerToken.objects.get(user=user, tracker=tracker)
        StravaDataGatherer().sync(user=user, token=token)
    except ObjectDoesNotExist:
        pass # If the token does not exists, the user does not have this tracker.

    except HTTPError as e:
        message = e.args[0]
        auth = tracker.auth_url
        messages.error(sender._request, 'Sorry!! We had issues authenticating your {0}. <a href="{1}">Please authenticate again.</a>'.format('Strava', auth))
