require.config({
  baseUrl: '/static/js',
  paths: {
    jquery: 'libs/jquery-2.1.4.min',
    underscore: 'libs/underscore.min',
    backbone: 'libs/backbone',
    handlebars: 'libs/handlebars'
  }
});

require(['views/trackers/trackerlistview'], function (TrackersView) {
	var feedView = new TrackersView();
});
