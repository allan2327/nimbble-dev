define([
  'jquery',
  'underscore',
  'backbone',
  // Pull in the Collection module from above
  'collections/trackers',
  'views/trackers/trackerview',
], function($, _, Backbone, TrackerCollection, TrackerView){
    var TrackersView = Backbone.View.extend({
        el: $("#feed-container"),
        initialize: function(){
            this.$loadingElt = $('#loading', this.$el);

            this.collection = new TrackerCollection();
            this.listenTo(this.collection, 'add', this.addOne);
            this.collection.fetch();
        },

        addOne: function(tracker){
            var view = new TrackerView({model: tracker});
            this.$el.append(view.render().el);
            this.$loadingElt.remove();
        },
    });
    // Returning instantiated views can be quite useful for having "state"
    return TrackersView;
});
