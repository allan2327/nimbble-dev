require.config({
  baseUrl: '/static/js',
  paths: {
    jquery: 'libs/jquery-2.1.4.min',
    underscore: 'libs/underscore.min',
    backbone: 'libs/backbone',
    handlebars: 'libs/handlebars'
  }
});

require(['views/activities/commfeed', 'views/users/userview', 'models/user', 'utils/setup'],
    function (ActivitiesView, UserView, User) {
	    var activitiesView = new ActivitiesView();

        var $profile = $('#user-profile');
        var user = new User({ id: $profile.data('user-id') });
        var userView = new UserView({ el: $('#user-profile'), model: user });

        user.fetch();
    }
);
