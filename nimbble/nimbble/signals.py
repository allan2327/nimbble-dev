from django.dispatch import Signal

sync_activities = Signal(providing_args=["user"])
