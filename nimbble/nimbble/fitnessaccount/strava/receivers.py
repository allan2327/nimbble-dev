from django.dispatch import receiver
from .signals import strava_activated
from stravalib.client import Client
from datetime import datetime, timedelta
from nimbble.models import FitnessActivity, CommunityActivityLink
import math

class QuadraticPointCalculator(object):

    COEFFICIENT = {
        'ride': 0.05,         # y = sqrt([(5)^2/500)]*x)
        'run': 0.2,           # y = sqrt([(10]^2/500]*x)
        'swim': 0.2,
    }

    def update_score(self, activity):
        type = activity.activity_type
        scale = self.COEFFICIENT.get(activity.activity_type.lower(), 0.01)
        score = math.sqrt(float(scale) * float(activity.average_watts))
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
        CommunityActivityLink.objects.create(community=default_comm, activity=new_activity)

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

        after = kwargs['after'] if 'after' in kwargs else datetime.now()
        activities = client.get_activities(after=after)

        converter = StravaActivityConverter(QuadraticPointCalculator())
        for strava_act in activities:
            converter.create_activity(user, strava_act)



@receiver(strava_activated)
def update_user_picture(sender, nimbble_token, **kwargs):
    user = nimbble_token.user
    StravaDataGatherer().set_picture(user, nimbble_token)


@receiver(strava_activated)
def update_user_activities_picture(sender, nimbble_token, **kwargs):
    after = datetime.now() - timedelta(days=60)
    StravaDataGatherer().sync(user=nimbble_token.user, token=nimbble_token.token, after=after)
