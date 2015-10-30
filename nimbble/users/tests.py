from django.test import TestCase
from users.models import User
from allauth.socialaccount.models import SocialAccount
from nimbble.models import FitnessActivity
from .receivers import FbSignalReceiver, update_user_score
from django.utils import timezone
from functools import reduce

class FbSignalHandlerTest(TestCase):

    def setUp(self):
        self.handler = FbSignalReceiver()
        self.user = User.objects.create_user(
            username='testuser', email='tuser@gmail.com', password='psw'
        )
        self.user.save()

    def test_new_user_with_fb_provider_correctly_sets_picture(self):
        pic_url = 'this.is.my.pic.jpg'
        acc = SocialAccount(provider='facebook', user=self.user)
        acc.extra_data['picture'] = { 'data': { 'url': pic_url } }
        acc.save()

        self.handler.new_user(self.user)

        self.assertEqual(pic_url, self.user.picture_url, 'Should set the picture url from the extra data parameter.')

    def test_new_user_set_user_name(self):
        self.user.username = None
        self.user.first_name = 'TestUser'
        acc = SocialAccount(provider='facebook', user=self.user)
        acc.extra_data['id'] = '1234'
        acc.save()

        self.handler.new_user(self.user)

        expected = '{}{}'.format(self.user.first_name.lower(), '1234')
        self.assertEqual(expected, self.user.username, 'Should set the user name using the id param and the user first name')

    def test_new_user_does_not_set_user_name_when_populated(self):
        acc = SocialAccount(provider='facebook', user=self.user)
        acc.extra_data['id'] = '1234'
        acc.save()

        old_username = self.user.username

        self.handler.new_user(self.user)

        self.assertEqual(old_username, self.user.username, 'Should not update the username.')

    def test_new_user_without_fb_provider_does_not_update_picture(self):
        self.user.picture_url = 'my.original.url'

        self.handler.new_user(self.user)

        self.assertEqual('my.original.url', self.user.picture_url)


class UpdateUserScoreReceiverTest(TestCase):
    def setUp(self):
        self.user = User.objects.create(username='testuser', email='tuser@gmail.com', password='psw')

    def test_update_user_score(self):
        activities = self.add_activities(4)
        update_user_score(None, user=self.user)

        scores = map(lambda a: a.score, activities)
        expected = reduce(lambda x, y:x+y, scores)
        self.assertEquals(expected, self.user.points)


    def add_activities(self, count):
        import random
        points = range(count)
        mult = random.randint(10, 100)
        return [self.create_activity(p*mult) for p in points]


    def create_activity(self, score):
        return FitnessActivity.objects.create(
            user=self.user,
            source_id=score,
            source_name='test',
            activity_type='test_at',
            average_watts=12.3,
            distance=12,
            moving_time=1,
            start_date=timezone.now(),
            score=score)













    def asdf(self):
        pass
