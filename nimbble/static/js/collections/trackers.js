define(['underscore','backbone','models/tracker'], function(_, Backbone, FitnessTracker){
    var TrackerCollection = Backbone.Collection.extend({
        model: FitnessTracker,
        url: '/api/v0/user/trackers/',
    });

    return TrackerCollection;
});
