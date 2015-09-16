from django.conf import settings
from django.conf.urls import url, patterns
from ui import views
# view imports
from django.views.generic import TemplateView

urlpatterns = patterns('ui.views',
    url(r'^feed/$', views.FeedView.as_view(), name='feed'),
    url(r'^trackers/$', views.TrackersView.as_view(), name='trackers'),
    url(r'', TemplateView.as_view(template_name='pages/home.html'), name='home'),
)
