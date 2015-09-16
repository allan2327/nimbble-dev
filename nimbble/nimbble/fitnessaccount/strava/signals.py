from django.dispatch import Signal

strava_activated = Signal(providing_args=["nimbble_token"])
