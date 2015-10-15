define(['underscore','backbone'], function(_, Backbone){
  var TrackerModel = Backbone.Model.extend({
    defaults: {
      name: '',
      active: false,
      description: '',
      icon_url: '',
      auth_url: '',
      tracker_link: '',
    }
  });

  return TrackerModel;
});
