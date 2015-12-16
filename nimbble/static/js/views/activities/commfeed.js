define([
  'jquery',
  'underscore',
  'backbone',
  'collections/activities',
  'views/activities/activityview',
  'views/activities/blankactivityview',
], function($, _, Backbone, ActivityCollection, ActivityView, BlankActivityView){
    var CommunityFeedView = Backbone.View.extend({
        el: $("#feed-container"),

        events: {
            'click a.loadmore': 'nextResultPage',
        },

        initialize: function(){
            var source = this.$el.data('source'),
                parentId = this.$el.data('source-id');

            // <div data-source="community" data-source-id="1"></div>
            this.collection = new ActivityCollection();
            this.collection.setUrl({ source: source, parentId: parentId });

            this.listenTo(this.collection, 'add', this.addOne);
            this.listenToOnce(this.collection, 'preParse', this.hideLoading);
            this.listenTo(this.collection, 'preParse', this.enableLoadMore);

            this.$feedList = $('.feed', this.el);
            this.$loadMore = $('#loadMore', this.el);

            this.collection.fetch();
        },

        nextResultPage: function(e){
            e.preventDefault(); e.stopPropagation();
            this.collection.requestNextPage();
        },

        hideLoading: function(){
            $('#loading', this.el).hide();
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
