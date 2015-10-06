from django.test import TestCase
from nimbble.models import FitnessTracker, FitnessTrackerAccount, FitnessTrackerToken, FitnessActivity
from users.models import User
from django.utils import timezone
from nimbble.serializers import UserTrackerSerializer, ActivitySerializer
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

class ActivitySerializerTest(TestCase):
    def setUp(self):
        self.user = User.objects.create(username='test1')
        self.activity = FitnessActivity()
        self.serializer = ActivitySerializer(self.activity)


    def test_meta_has_correct_model(self):
        self.assertTrue(self.serializer.Meta.model is FitnessActivity)


    def test_meta_includes_correct_fields(self):
        expected = ('user','source_id','source_name','activity_type','average_watts','distance','moving_time', 'duration', 'score', 'activity_date',)
        fields = self.serializer.Meta.fields
        self.assertTrue(fields == expected)


    def test_get_duration_string(self):
        self.activity.moving_time = 4521 # moving time in seconds

        result = self.serializer.get_duration_string(self.activity)
        expected = '{:02}:{:02}:{:02}'.format(1, 15, 21)

        self.assertEquals(result, expected)


    def test_get_date_str_correct_format(self):
        self.activity.start_date = timezone.now()

        result = self.serializer.get_date_str(self.activity)
        expected = self.activity.start_date.strftime('%a %b %d, %Y')

        self.assertEquals(result, expected)


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
