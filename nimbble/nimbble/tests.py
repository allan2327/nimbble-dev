from django.test import TestCase
from nimbble.models import FitnessTracker, AuthTracker
from users.models import User
from nimbble.serializers import UserTrackerSerializer
# Create your tests here.


class UserTrackerSerializerTestCase(TestCase):
    def setUp(self):
        self.user = User(username='test1')
        self.tracker = FitnessTracker(name='strava')
        self.serializer = UserTrackerSerializer(self.tracker, user=self.user)
        self.user.save()
        self.tracker.save()


    def test_meta_has_correct_model(self):
        self.assertTrue(self.serializer.Meta.model is FitnessTracker)


    def test_meta_includes_correct_fields(self):
        expected = ('id', 'name', 'description', 'icon_url', 'auth_url', 'tracker_link', 'active')
        fields = self.serializer.Meta.fields
        self.assertTrue(fields == expected)


    def test_get_active_status_user_has_auth_tracker(self):
        auth_tracker = AuthTracker(user=self.user, tracker=self.tracker)
        auth_tracker.save()

        active = self.serializer.get_active_status(self.tracker)

        self.assertTrue(active)


    def test_get_active_status_user_does_not_have_auth_tracker(self):
        tracker2 = FitnessTracker(name='other-tracker')
        tracker2.save()
        auth_tracker = AuthTracker(user=self.user, tracker=tracker2)
        auth_tracker.save()

        active = self.serializer.get_active_status(self.tracker)

        self.assertFalse(active)
