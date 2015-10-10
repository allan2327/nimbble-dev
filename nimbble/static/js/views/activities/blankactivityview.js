define([
  'jquery',
  'handlebars',
  'backbone',
  'text!/static/frontend/fe_empty_activity.html'
], function($, Handlebars, Backbone, activityTemplate){
    var ActivityView = Backbone.View.extend({

        template: Handlebars.compile(activityTemplate),

        render: function() {
            this.$el.html(this.template());
            return this;
        },
    });
    return ActivityView;
});
