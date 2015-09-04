from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^strava/login/token/$', views.token_login, name='strava_token_login'),
]
