define([
  'jquery',
  'handlebars',
  'backbone',
  'text!/static/frontend/fe_tracker.html'
], function($, Handlebars, Backbone, trackerTemplate){
    var MessageView = Backbone.View.extend({

        tagName: 'li',
        template: Handlebars.compile(trackerTemplate),

        render: function() {
            this.$el.html(this.template(this.model.toJSON()));
            return this;
        },

    });

    return MessageView;
});
