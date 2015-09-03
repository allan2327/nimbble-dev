from django.contrib import admin
from .models import Community, FitnessTracker, FitnessTrackerAccount, FitnessTrackerToken

# Register your models here.
admin.site.register(Community)
admin.site.register(FitnessTracker)
admin.site.register(FitnessTrackerAccount)
admin.site.register(FitnessTrackerToken)
