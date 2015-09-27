require(['views/activities/commfeed'], function (CommunityFeedView) {
	return {
		initialize: function(){
			var feedView = new CommunityFeedView();
			feedView.initialize();
		}
	};
});
