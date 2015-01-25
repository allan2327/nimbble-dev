from django.test import TestCase

from django import forms
from authutils.adapter import BasicEmailAccountAdapter
from authutils.models import AuthorizedEmail


class BasicEmailAccountAdapterTest(TestCase):

    def setUp(self):
        self.adapter = BasicEmailAccountAdapter()

    def test_clean_email_with_whitelisted_postfix(self):
        postfix = 'something.com'
        email = AuthorizedEmail(email_postfix=postfix)
        email.save()

        test_email = '{0}@{1}'.format('username', postfix)
        result = self.adapter.clean_email(test_email)

        self.assertEqual(result, test_email)


    def test_clean_email_with_nonwhitelisted_postfix_throws_validation_error(self):
        test_email = 'username@nothing.com'

        try:
            self.adapter.clean_email(test_email)
        except forms.ValidationError as ve:
            msg = 'Invalid email. Please make sure your company has a nimbble account.'
            self.assertEqual(ve.message, msg)








