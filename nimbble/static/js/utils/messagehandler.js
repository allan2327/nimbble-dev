define([
  'jquery',
  'underscore',
  'views/utils/dynamicview'
], function($, _, DynamicView){
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
            !!data.messages ? self.HandleMultipleMessages(data) : self.HandleSingleMessage(data);
        };

        this.HandleMultipleMessages = function(data){
            var msgs = _.groupBy(data.messages, function(messageObj){ return messageObj.tags; });
            var view = new DynamicView({model: { messages: msgs }});
            view.setTemplate('message-list')
                .onRender(function(newElt){ self.$el.append(newElt); });
        };

        this.HandleSingleMessage = function(data){
            var tag = data.success ? 'success' : 'danger';

            var view = new DynamicView({model: { tag: tag, message: data.message }});
            view.setTemplate('message')
                .onRender(function(newEl){ self.$el.append(newEl); });
        };
    };

    return MessageHandler;
});
