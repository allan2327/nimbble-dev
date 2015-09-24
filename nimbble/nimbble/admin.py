from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(Community)
admin.site.register(FitnessTracker)
admin.site.register(FitnessTrackerAccount)
admin.site.register(FitnessTrackerToken)
admin.site.register(FitnessActivity)
admin.site.register(CommunityActivityLink)
