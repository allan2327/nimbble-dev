define([
  'underscore',
  'backbone'
], function(_, Backbone){
  var ActivityModel = Backbone.Model.extend({
    defaults: {
      user: {},
      source_id: '',
      source_name: '',
      activity_type: '',
      average_watts: '',
      distance: '',
      moving_time: '',
      score: '',
      created: ''
    }
  });
  // Return the model for the module
  return ActivityModel;
});
