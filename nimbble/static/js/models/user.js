define(['underscore', 'backbone'], function(_, Backbone){
  var UserModel = Backbone.Model.extend({
        urlRoot: '/api/v0/users',
        defaults: {
            id: '',
            picture_url: '',
            points: '',
            user_name: '',
            first_name: '',
            last_name: '',
            tag_line: '',
            about_me: '',
        }
  });

  return UserModel;
});
