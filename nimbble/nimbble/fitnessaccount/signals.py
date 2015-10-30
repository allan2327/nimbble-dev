from django.dispatch import Signal

activities_loaded = Signal(providing_args=["user"])
