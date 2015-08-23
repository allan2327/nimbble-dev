from rest_framework import serializers
from rest_framework.fields import empty
from nimbble.models import Community, FitnessTracker, AuthTracker


class CommunitySerializer(serializers.ModelSerializer):
    class Meta:
        model = Community
        fields = ('id', 'name', 'city', 'state')


class TrackerSerializer(serializers.ModelSerializer):
    class Meta:
        model = FitnessTracker
        fields = ('id', 'name', 'description', 'icon_url', 'auth_url', 'tracker_link', 'active')


class UserTrackerSerializer(serializers.ModelSerializer):

    def __init__(self, instance=None, data=empty, user=None, **kwargs):
        super(serializers.ModelSerializer, self).__init__(instance, data, **kwargs)
        self.user = user

    active = serializers.SerializerMethodField('get_active_status')

    def get_active_status(self, tracker):
        return AuthTracker.objects.filter(user=self.user, tracker=tracker).exists()

    class Meta:
        model = FitnessTracker
        fields = ('id', 'name', 'description', 'icon_url', 'auth_url', 'tracker_link', 'active')
