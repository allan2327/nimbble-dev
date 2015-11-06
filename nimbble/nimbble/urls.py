from django.conf.urls import url, include
from rest_framework.urlpatterns import format_suffix_patterns
from nimbble import views

urlpatterns = [
    url(r'^communities/$', views.CommunityList.as_view()),
    url(r'^community/(?P<pk>[0-9]+)/$', views.CommunityDetail.as_view()),
    url(r'^community/(?P<pk>[0-9]+)/activities/$', views.CommunityActivityFeedList.as_view()),
    url(r'^user/(?P<pk>[0-9]+)/activities/$', views.UserActivityFeedList.as_view()),
    url(r'^user/trackers/$', views.UserTrackerList.as_view()),
    url(r'^user/sync/$', views.UserSync.as_view(), name='user_sync'),

    url(r'^trackers/$', views.TrackerList.as_view()),
    url(r'^tracker/deactivate/$', views.DeactivateTrackerDetail.as_view()),
    url(r'^tracker/(?P<pk>[0-9]+)/$', views.TrackerDetail.as_view()),


    url(r'', include('nimbble.fitnessaccount.strava.urls')),
    url(r'', include('nimbble.fitnessaccount.fitbit.urls')),
]

urlpatterns = format_suffix_patterns(urlpatterns)
