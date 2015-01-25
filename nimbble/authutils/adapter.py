
from allauth.account.adapter import DefaultAccountAdapter
from django.utils.translation import ugettext_lazy as _
from django import forms
from .models import AuthorizedEmail


class BasicEmailAccountAdapter(DefaultAccountAdapter):

    def clean_email(self, email):

        postfix = email[email.index('@')+1:]

        if AuthorizedEmail.objects.filter(email_postfix=postfix).exists():
            return email

        raise forms.ValidationError(_("Invalid email. Please make sure your company has a nimbble account."))


