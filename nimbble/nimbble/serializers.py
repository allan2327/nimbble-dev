from rest_framework import serializers
from rest_framework.fields import empty
from nimbble.models import Community, FitnessTracker, FitnessActivity, FitnessTrackerToken
from users.models import User

class SimpleUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'picture_url', 'points', 'username', 'first_name')


class CommunitySerializer(serializers.ModelSerializer):
    class Meta:
        model = Community
        fields = ('id', 'name', 'city', 'state')


class TrackerSerializer(serializers.ModelSerializer):
    class Meta:
        model = FitnessTracker
        fields = ('id', 'name', 'description', 'icon_url', 'auth_url', 'tracker_link')


class ActivitySerializer(serializers.ModelSerializer):

    user = serializers.SerializerMethodField('get_user_data')
    duration = serializers.SerializerMethodField('get_duration_string')
    activity_date = serializers.SerializerMethodField('get_date_str')

    def get_duration_string(self, activity):
        secs = activity.moving_time % 60
        mins = (activity.moving_time / 60) % 60
        hours = activity.moving_time / 3600

        return '{:02}:{:02}:{:02}'.format(int(hours), int(mins), secs)

    def get_user_data(self, activity):
        user_ser = SimpleUserSerializer(activity.user)
        return user_ser.data

    def get_date_str(self, activity):
        return activity.start_date.strftime('%a %b %d, %Y')

    class Meta:
        model = FitnessActivity
        fields = ('user','source_id','source_name','activity_type','average_watts','distance','moving_time', 'duration', 'score', 'activity_date',)

class UserTrackerSerializer(serializers.ModelSerializer):

    def __init__(self, instance=None, data=empty, user=None, **kwargs):
        super(serializers.ModelSerializer, self).__init__(instance, data, **kwargs)
        self.user = user

    active = serializers.SerializerMethodField('get_active_status')

    def get_active_status(self, tracker):
        return FitnessTrackerToken.objects.filter(user=self.user, tracker=tracker).exists()

    class Meta:
        model = FitnessTracker
        fields = ('id', 'name', 'description', 'icon_url', 'auth_url', 'tracker_link', 'active')
