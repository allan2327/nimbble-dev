
define(['utils/messagehandler', 'utils/slimbstrap', 'utils/setcsrftoken'],
    function(MessageHandler, SlimBstrap){
        var $cont = $('.js-content-container');

        var msgHandler = new MessageHandler($cont);
        msgHandler.Init();

        var bstrap = new SlimBstrap($cont);
        bstrap.Init();
    }
);
