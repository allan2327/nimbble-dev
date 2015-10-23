
define(['jquery'], function($){

    return {
        post: function(msg){
            var view = msg.view;
            return $.post(msg.url, msg.data)
                .done(function(data){
                    view.$el.trigger('UpdateStatus', data);
                });
        },


    };
});
