# -*- coding: utf-8 -*-
# Import the reverse lookup function
from django.core.urlresolvers import reverse

# view imports
from django.views.generic import TemplateView, RedirectView

# Only authenticated users can access views using this.
from braces.views import LoginRequiredMixin
from nimbble.models import FitnessTracker
from nimbble.serializers import UserTrackerSerializer
from nimbble.utils import get_current_community
from users.models import User

class FeedView(LoginRequiredMixin, TemplateView):
    loading_message = 'Retrieving recent activities.'
    template_name = 'pages/home.html'

    def get_context_data(self, **kwargs):
        comm = get_current_community(self.request)

        return { 'feed_view': 'active', 'parent_id': comm.id, 'loading_message': self.loading_message }


class AthleteView(LoginRequiredMixin, TemplateView):
    template_name = 'ui/athlete.html'

    def get_context_data(self, **kwargs):
        comm = get_current_community(self.request)
        user = User.objects.get(pk=kwargs.get('user_id'))
        return { 'athlete_view': 'active', 'parent_id': comm.id, 'user': user }


class TrackersView(LoginRequiredMixin, TemplateView):
    loading_message = 'Retrieving your fitness trackers.'
    template_name = 'ui/trackers.html'

    def get_context_data(self, **kwargs):
        user = self.request.user
        trackers = FitnessTracker.objects.all()
        serializer = UserTrackerSerializer(trackers, many=True, user=user)
        return { 'tracker_view': 'active', 'trackers': serializer.data, 'loading_message': self.loading_message }


class SignInRedirect(RedirectView):
    permanent = False

    def get_redirect_url(self):
        return reverse("account_login")
