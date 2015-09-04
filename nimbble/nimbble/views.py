from nimbble.models import Community, FitnessTracker
from nimbble.serializers import CommunitySerializer, TrackerSerializer, UserTrackerSerializer
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.views import APIView

class CommunityList(generics.ListCreateAPIView):
    queryset = Community.objects.all()
    serializer_class = CommunitySerializer

class CommunityDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Community.objects.all()
    serializer_class = CommunitySerializer

class TrackerList(generics.ListCreateAPIView):
    queryset = FitnessTracker.objects.all()
    serializer_class = TrackerSerializer

class TrackerDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = FitnessTracker.objects.all()
    serializer_class = TrackerSerializer

class UserTrackerList(APIView):
    def get(self, request, format=None):
        user = request.user
        trackers = FitnessTracker.objects.all()
        serializer = UserTrackerSerializer(trackers, many=True, user=user)
        return Response(serializer.data)
