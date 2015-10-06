from django.test import TestCase
from nimbble.models import Community, FitnessActivity
from users.models import User
from django.utils import timezone
# Create your tests here.

class TestCommunityACtivityRelationship(TestCase):


    def test_relationships(self):
        commA = Community.objects.create(name='samsung')
        commB = Community.objects.create(name='frutti')

        u1 = self.get_user(commA, 'user1')
        u2 = self.get_user(commA, 'user2')
        u3 = self.get_user(commB, 'user3')

        self.add_activities(u1, 4)
        self.add_activities(u2, 5)
        self.add_activities(u3, 2)

        acts_for_user1 = FitnessActivity.objects.filter(user=u1)
        self.assertEqual(4, len(acts_for_user1))


    def get_user(self, community, username):
        new_user = User.objects.create(username=username)
        new_user.communities.add(community)
        new_user.save()
        return new_user



    def add_activities(self, user, count):
        for i in range(count):
            self.add_activity(user, i)

    def add_activity(self, user, source_id):
        return FitnessActivity.objects.create(
            user=user,
            source_id=source_id,
            start_date=timezone.now(),
            source_name='s1',
            activity_type='a1',
            distance=1,
            moving_time=1,
            average_watts=12.4,
            score=10)













def asdf():
    pass
