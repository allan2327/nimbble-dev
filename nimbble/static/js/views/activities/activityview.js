define([
  'jquery',
  'handlebars',
  'backbone',
  // Pull in the Collection module from above
  'text!/static/frontend/fe_activity.html'
], function($, Handlebars, Backbone, activityTemplate){
    var ActivityView = Backbone.View.extend({

        tagName: 'li',
        template: Handlebars.compile(activityTemplate),

        render: function() {
            this.$el.html(this.template(this.model.toJSON()));
            return this;
        },

    });
    // Returning instantiated views can be quite useful for having "state"
    return ActivityView;
});
