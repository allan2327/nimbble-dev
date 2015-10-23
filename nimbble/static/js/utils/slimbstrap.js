
define(['jquery'], function($){

    var GlobalHandler = function($el){
        var self = this;
        this.$el = $el;

        this.Init = function(){
            this.AttachEvents();
        };

        this.AttachEvents = function(){
            this.$el.on('click', '.close', self.HandleClose);
        };

        this.HandleClose = function(e){
            var $target = $(e.target).closest('.close');
            $target.closest('.'+$target.data('dismiss')).remove();
        };
    };

    return GlobalHandler;
});
