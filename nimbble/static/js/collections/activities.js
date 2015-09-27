define(['underscore','backbone','models/activity'], function(_, Backbone, ActivityModel){
    var ActivityCollection = Backbone.Collection.extend({
        model: ActivityModel,

        parse: function(request){
            return request.results;
        },
    });
    // You don't usually return a collection instantiated
    return ActivityCollection;
});
