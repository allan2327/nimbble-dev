define(['underscore','backbone','models/activity'], function(_, Backbone, ActivityModel){
    var ActivityCollection = Backbone.Collection.extend({
        model: ActivityModel,

        hasNextPage: function(){ return !!this.nextUrl; },
        hasPrevPage: function(){ return !!this.prevUrl; },

        parse: function(request){
            this.nextUrl = request.next;
            this.prevUrl = request.previous;

            this.trigger('preParse')
            return request.results;
        },
    });

    return ActivityCollection;
});
