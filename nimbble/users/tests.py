from django.test import TestCase
from users.models import User
from allauth.socialaccount.models import SocialAccount
from .receivers import FbSignalReceiver

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
