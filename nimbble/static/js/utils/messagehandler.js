define([
  'jquery',
  'views/utils/dynamicview'
], function($, DynamicView){
    var MessageHandler = function($cont){
        var self = this;
        this.$cont = $cont;
        
        this.Init = function(){
            this.$el = $('.js-msg-container');
            this.AttachEvents();
        };

        this.AttachEvents = function(){
            this.$cont.on('UpdateStatus', this.HandleStatusUpdate);
        };

        this.HandleStatusUpdate = function(e, data){
            var tag = data.success ? 'success' : 'danger';

            var view = new DynamicView({model: { tag: tag, message: data.message }});
            view.setTemplate('message')
                .onRender(function(newEl){ self.$el.append(newEl); });
        };
    };

    return MessageHandler;
});
