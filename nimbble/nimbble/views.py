from nimbble.models import Community, FitnessTracker, CommunityActivityLink, FitnessActivity, FitnessTrackerToken
from nimbble import serializers
from rest_framework import generics
from rest_framework.serializers import ValidationError
from rest_framework.response import Response
from rest_framework.views import APIView

class CommunityList(generics.ListCreateAPIView):
    queryset = Community.objects.all()
    serializer_class = serializers.CommunitySerializer


class CommunityDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Community.objects.all()
    serializer_class = serializers.CommunitySerializer


class CommunityActivityFeedList(generics.ListAPIView):
    serializer_class = serializers.ActivitySerializer

    def get_queryset(self):
        communityId = self.kwargs.get('pk')
        return FitnessActivity.objects.filter(community_link__community=communityId).order_by('-start_date')


class UserActivityFeedList(generics.ListAPIView):
    serializer_class = serializers.ActivitySerializer

    def get_queryset(self):
        userId = self.kwargs.get('pk')
        return FitnessActivity.objects.filter(user=userId).order_by('-start_date')


class TrackerList(generics.ListAPIView):
    queryset = FitnessTracker.objects.all()
    serializer_class = serializers.TrackerSerializer


class TrackerDetail(generics.RetrieveAPIView):
    queryset = FitnessTracker.objects.all()
    serializer_class = serializers.TrackerSerializer

from django.core.exceptions import ObjectDoesNotExist
class DeactivateTrackerDetail(APIView):
    http_method_names = ['post']
    def post(self, request, format=None):
        user = request.user
        tracker_id = request.POST.get('token_id', '')

        if len(tracker_id) == 0:
            return Response({ 'success': False, 'message': 'Invalid tracker id.' })

        try:
            token = FitnessTrackerToken.objects.get(pk=int(tracker_id))
            token.delete()
        except ObjectDoesNotExist:
            return Response({ 'success': False, 'message': 'Invalid tracker id.' })

        message = 'You have successfully deactivated {}.'.format(token.tracker.name)
        return Response({ 'success': True, 'message': message })


class UserTrackerList(APIView):
    def get(self, request, format=None):
        user = request.user
        trackers = FitnessTracker.objects.all()
        serializer = serializers.UserTrackerSerializer(trackers, many=True, user=user)
        return Response(serializer.data)
