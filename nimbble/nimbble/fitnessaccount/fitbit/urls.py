from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^fitbit/login/token/$', views.token_login, name='fitbit_token_login'),
]
