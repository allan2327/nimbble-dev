define(['underscore','backbone','models/activity'], function(_, Backbone, ActivityModel){

    var UrlParser = {
        getSearchParam: function(url){
            if(!url) return null;

            var parser = document.createElement('a');
            parser.href = url;
            return parser.search;
        },
    };

    var ActivityCollection = Backbone.Collection.extend((function(){

        var _origUrl = '',
            _nextParam = null,
            _prevParam = null;

        return {
            model: ActivityModel,

            hasNextPage: function(){ return !!_nextParam; },
            hasPrevPage: function(){ return !!_prevParam; },
            setUrl: function(data){
                // api/v0/community/1/activities/
                _origUrl = this.url = '/api/v0/'+data.source+'/'+data.parentId+'/activities/';
            },

            requestNextPage: function(){
                this.url = _origUrl + _nextParam;
                this.fetch();
            },

            /*
                count: 15
                next: "http://localhost:8000/api/v0/community/1/activities/?page=3"
                previous: "http://localhost:8000/api/v0/community/1/activities/"
                results: []
            */
            parse: function(request){
                _nextParam = UrlParser.getSearchParam(request.next);
                _prevParam = UrlParser.getSearchParam(request.previous);

                this.trigger('preParse');
                return request.results;
            },
        };
    })());

    return ActivityCollection;
});
