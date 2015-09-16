from django.conf.urls import url
from . import views, receivers

urlpatterns = [
    url(r'^strava/login/token/$', views.StravaTokenRedirectView.as_view(), name='strava_token_login'),
]
