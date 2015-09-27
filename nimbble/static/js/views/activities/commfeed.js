define([
  'jquery',
  'underscore',
  'backbone',
  // Pull in the Collection module from above
  'collections/activities',
  'views/activities/activityview',
], function($, _, Backbone, ActivityCollection, ActivityView){
    var CommunityFeedView = Backbone.View.extend({
        el: $("#feed-container"),
        initialize: function(){
            var parentId = this.$el.data('parent-id');
            this.collection = new ActivityCollection();
            this.collection.url = '/api/v0/community/'+parentId+'/activities/';

            this.listenTo(this.collection, 'add', this.addOne);
            this.listenTo(this.collection, 'reset', this.addAll);
            this.listenTo(this.collection, 'all', this.render);

            this.$empty = $('#empty', this.el);
            this.$feedList = $('.feed', this.el);

            this.collection.fetch();
        },

        render: function(){
            if(this.collection.length){
                this.$empty.hide();
            }
        },

        addOne: function(activity){
            var view = new ActivityView({model: activity});
            this.$feedList.append(view.render().el);
        },

        addAll: function(){
            this.collection.each(this.addOne, this);
        },
    });
    // Returning instantiated views can be quite useful for having "state"
    return CommunityFeedView;
});
