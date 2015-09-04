# -*- coding: utf-8 -*-
# Import the reverse lookup function
from django.core.urlresolvers import reverse

# view imports
from django.views.generic import TemplateView, RedirectView

# Only authenticated users can access views using this.
from braces.views import LoginRequiredMixin
from nimbble.models import FitnessTracker
from nimbble.serializers import UserTrackerSerializer

def auth_handler():
    pass


class FeedView(LoginRequiredMixin, TemplateView):
    template_name = 'pages/home.html'


class TrackersView(LoginRequiredMixin, TemplateView):
    template_name = 'ui/trackers.html'

    def get_context_data(self, **kwargs):
        user = self.request.user
        trackers = FitnessTracker.objects.all()
        serializer = UserTrackerSerializer(trackers, many=True, user=user)
        return { 'trackers': serializer.data }


class SignInRedirect(RedirectView):
    permanent = False

    def get_redirect_url(self):
        return reverse("account_login")
