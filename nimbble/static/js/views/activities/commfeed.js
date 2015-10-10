define([
  'jquery',
  'underscore',
  'backbone',
  // Pull in the Collection module from above
  'collections/activities',
  'views/activities/activityview',
  'views/activities/blankactivityview',
], function($, _, Backbone, ActivityCollection, ActivityView, BlankActivityView){
    var CommunityFeedView = Backbone.View.extend({
        el: $("#feed-container"),
        initialize: function(){
            var source = this.$el.data('source'),
                parentId = this.$el.data('source-id');

            this.collection = new ActivityCollection();
            this.collection.url = '/api/v0/'+source+'/'+parentId+'/activities/';

            this.listenTo(this.collection, 'add', this.addOne);
            this.listenTo(this.collection, 'reset', this.addAll);
            this.listenTo(this.collection, 'all', this.render);

            this.$loading = $('#loading', this.el);
            this.$feedList = $('.feed', this.el);

            this.collection.fetch();
        },

        render: function(){
            this.$loading.hide();
            if(!this.collection.length){
                var blankView = new BlankActivityView({model: {}});
                this.$feedList.html(blankView.render().el);
            }else{
                $('#empty', this.el).remove();
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
