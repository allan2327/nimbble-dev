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
            this.listenTo(this.collection, 'all', this.render);
            this.listenTo(this.collection, 'preParse', this.enableLoadMore);

            this.$loading = $('#loading', this.el);
            this.$feedList = $('.feed', this.el);
            this.$loadMore = $('#loadMore', this.el);

            this.collection.fetch();
        },

        render: function(){
            this.$loading.hide();
        },

        enableLoadMore: function(){
            if(this.collection.hasNextPage())
                this.$loadMore.removeClass('hidden');
            else
                this.$loadMore.addClass('hidden');
        },

        addOne: function(activity){
            var view = new ActivityView({model: activity});
            this.$feedList.append(view.render().el);
        },
    });

    return CommunityFeedView;
});
