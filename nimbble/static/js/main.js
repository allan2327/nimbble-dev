require.config({
  baseUrl: '/static/js',
  paths: {
    jquery: 'libs/jquery-2.1.4.min',
    underscore: 'libs/underscore.min',
    backbone: 'libs/backbone',
    handlebars: 'libs/handlebars'
  }
});

require(['utils/setcsrftoken', 'views/activities/commfeed'], function (t, CommunityFeedView) {
	var feedView = new CommunityFeedView();
});
