define([
  'jquery',
  'handlebars',
  'backbone',
  'utils/dispatcher',
  'text!/static/frontend/fe_tracker.html'
], function($, Handlebars, Backbone, Dispatcher, trackerTemplate){
    var TrackerView = Backbone.View.extend({

        tagName: 'li',
        template: Handlebars.compile(trackerTemplate),
        events: {
            'click .js-deactivate': 'deactivateTracker',
        },

        deactivateTracker: function(e){
            var msg = {
                url: '/api/v0/tracker/deactivate/',
                data: { token_id: $(e.target).data('token') },
                view: this,
            };

            Dispatcher.post(msg)
                .success(this.resetActionStatus);
        },

        resetActionStatus: function(d){
            if(!d.success) return;

            this.$el.find('.js-deactivate').remove();
            this.$el.find('.js-active').removeClass('hidden');
        },

        render: function() {
            this.$el.html(this.template(this.model.toJSON()));
            return this;
        },

    });

    return TrackerView;
});
