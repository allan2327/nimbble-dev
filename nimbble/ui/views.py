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
    template_name = 'pages/home.html'

class TrackersView(LoginRequiredMixin, TemplateView):
    template_name = 'ui/trackers.html'

    def get_context_data(self, **kwargs):
        trackers = self.get_trackers()
        return { 'trackers': trackers }

    def get_trackers(self):
        return [
            { 'name': 'strava1', 'icon_url': '/static/images/128.png', 'tracker_link': 'http://google.com', 'description': 'descr' },
            { 'name': 'strava2', 'icon_url': '/static/images/128.png', 'tracker_link': 'http://google.com', 'description': 'descr' },
            { 'name': 'strava3', 'icon_url': '/static/images/128.png', 'tracker_link': 'http://google.com', 'description': 'descr' },
        ]

class SignInRedirect(RedirectView):
    permanent = False

    def get_redirect_url(self):
        return reverse("account_login")
