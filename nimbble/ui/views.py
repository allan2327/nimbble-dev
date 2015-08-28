# -*- coding: utf-8 -*-
# Import the reverse lookup function
from django.core.urlresolvers import reverse

# view imports
from django.views.generic import TemplateView, RedirectView

# Only authenticated users can access views using this.
from braces.views import LoginRequiredMixin

def auth_handler():
    pass

class FeedView(LoginRequiredMixin, TemplateView):
    template_name = 'home.html'


class SignInRedirect(RedirectView):
    permanent = False

    def get_redirect_url(self):
        return reverse("account_login")
