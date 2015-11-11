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
            e.stopPropagation(); e.preventDefault();
            var msg = {
                url: '/api/v0/user/sync/',
                view: this,
            };

            var update = this.updateActivities.bind(this);
            Dispatcher.post(msg).success(update);
        },

        updateActivities: function(d){
            if(!d.success) return;

            //this.$el.find('.js-deactivate').remove();
            //this.$el.find('.js-active').removeClass('hidden');
        },

        render: function() {
            this.$el.html(this.template(this.model.toJSON()));
            return this;
        },

    });

    return UserView;
});
