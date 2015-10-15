from nimbble.models import Community, FitnessTracker, CommunityActivityLink, FitnessActivity
from nimbble import serializers
from rest_framework import generics
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


class TrackerList(generics.ListCreateAPIView):
    queryset = FitnessTracker.objects.all()
    serializer_class = serializers.TrackerSerializer


class TrackerDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = FitnessTracker.objects.all()
    serializer_class = serializers.TrackerSerializer


class UserTrackerList(APIView):
    def get(self, request, format=None):
        user = request.user
        trackers = FitnessTracker.objects.all()
        serializer = serializers.UserTrackerSerializer(trackers, many=True, user=user)
        return Response(serializer.data)
