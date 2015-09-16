from django.dispatch import receiver
from .signals import strava_activated
from stravalib.client import Client

@receiver(strava_activated)
def activated_update_user_picture(sender, nimbble_token, **kwargs):
    user = nimbble_token.user

    if len(user.picture_url) != 0 and '128.png' not in user.picture_url:
        return

    client = Client(access_token=nimbble_token.token)
    athlete = client.get_athlete()

    user.picture_url = athlete.profile_medium
    user.save()
