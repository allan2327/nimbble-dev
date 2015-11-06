define([
  'jquery',
  'handlebars',
  'backbone',
  'utils/dispatcher',
  'text!/static/frontend/fe_user.html'
], function($, Handlebars, Backbone, Dispatcher, userTemplate){
    var UserView = Backbone.View.extend({
        template: Handlebars.compile(userTemplate),
        events: {
            'click .js-sync': 'syncActivities',
        },

        initialize: function(){
            this.listenTo(this.model, 'sync', this.render);
        },

        syncActivities: function(e){
            var msg = {
                url: '/api/v0/tracker/deactivate/',
                data: { token_id: $(e.target).data('token') },
                view: this,
            };

            var reset = this.resetActionStatus.bind(this);
            Dispatcher.post(msg).success(reset);
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

    return UserView;
});
