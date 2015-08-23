from django.conf import settings
from django.conf.urls import url, patterns
from ui import views
# view imports
from django.views.generic import TemplateView

urlpatterns = patterns('ui.views',
    url(r'', views.SignInRedirect.as_view(), name='home'),   
    url(r'^feed/$', views.FeedView.as_view(), name='feed'),
)
