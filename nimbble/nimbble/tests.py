from django.test import TestCase
from nimbble.models import FitnessTracker, FitnessTrackerAccount, FitnessTrackerToken
from users.models import User
from nimbble.serializers import UserTrackerSerializer
# Create your tests here.


class UserTrackerSerializerTest(TestCase):
    def setUp(self):
        self.user = User.objects.create(username='test1')
        self.tracker = FitnessTracker.objects.create(name='strava')
        self.serializer = UserTrackerSerializer(self.tracker, user=self.user)


    def test_meta_has_correct_model(self):
        self.assertTrue(self.serializer.Meta.model is FitnessTracker)


    def test_meta_includes_correct_fields(self):
        expected = ('id', 'name', 'description', 'icon_url', 'auth_url', 'tracker_link', 'active')
        fields = self.serializer.Meta.fields
        self.assertTrue(fields == expected)


    def test_get_active_status_user_has_auth_tracker(self):
        FitnessTrackerToken.objects.create(user=self.user, tracker=self.tracker)
        active = self.serializer.get_active_status(self.tracker)
        self.assertTrue(active)


    def test_get_active_status_user_does_not_have_auth_tracker(self):
        tracker2 = FitnessTracker.objects.create(name='other-tracker')
        FitnessTrackerToken.objects.create(user=self.user, tracker=tracker2)

        active = self.serializer.get_active_status(self.tracker)

        self.assertFalse(active)



class SimpleTrackerFlowTest(TestCase):

    def setUp(self):
        pass


    def test_workflow(self):
        strava = FitnessTracker.objects.create(name='strava', icon_url='stv.png', tracker_link='strava.com')

        strava_acc = FitnessTrackerAccount.objects.create(tracker=strava, app_id='24341', app_secret='asdfoernwer234fo234n23kln23')

        user1 = User.objects.create(username='testuser1')
        user2 = User.objects.create(username='testuser2')

        token1 = FitnessTrackerToken.objects.create(user=user1, tracker=strava, token='h23h23k4j2o3k4j')
        token2 = FitnessTrackerToken.objects.create(user=user2, tracker=strava, token='jkl32j4l23kj4o2')

        self.assertTrue(True)


















    def somethin(self):
        pass
