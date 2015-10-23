define([
  'jquery',
  'handlebars',
  'backbone',
  'require'
], function($, Handlebars, Backbone, require_ctx){
    var GenericView = Backbone.View.extend({
        setTemplate: function(name){
            this.templateName = name;
            return this;
        },

        onRender: function(callback){
            if(!!this.template){
                this.render();
                callback(this.el);
                return this;
            }

            var view = this;
            var templateToGet = 'text!/static/frontend/fe_'+this.templateName+'.html';
            require_ctx([templateToGet], function(templateText){
                view.template = Handlebars.compile(templateText);
                view.render();
                callback(view.el);
            });

            return this;
        },

        render: function() {
            this.$el.html(this.template(this.model));
            return this;
        },
    });

    return GenericView;
});
