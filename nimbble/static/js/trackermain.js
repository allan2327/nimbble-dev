require.config({
  baseUrl: '/static/js',
  paths: {
    jquery: 'libs/jquery-2.1.4.min',
    underscore: 'libs/underscore.min',
    backbone: 'libs/backbone',
    handlebars: 'libs/handlebars'
  }
});

require(['jquery', 'views/trackers/trackerlistview'], function ($, TrackersView) {

    var csrftoken = $('[name="csrfmiddlewaretoken"]').val();
    function csrfSafeMethod(method) {
        // these HTTP methods do not require CSRF protection
        return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
    }
    $.ajaxSetup({
        beforeSend: function(xhr, settings) {
            if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
                xhr.setRequestHeader("X-CSRFToken", csrftoken);
            }
        }
    });

	var feedView = new TrackersView();
});
