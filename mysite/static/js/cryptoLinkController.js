App.controller('cryptoLinkController',['$scope', '$rootScope','$http','$q', function($scope, $rootScope, $http, $q) {

    $scope.loadMoreElements = true;
    $scope.startLoadingMoreElements = true;

    $scope.initial = function(sUrl, sTitle, sDesc){
        $scope.sUrl = sUrl;
        $scope.sTitle = sTitle;
        $scope.sDesc = sDesc;
    };

    $scope.initialise = function(json){
        $scope.data = json;
        console.log($scope.data);
        console.log($scope.data.breadcrumbs);
        //TODO followers count calculation
    };

    $scope.upvote = function(cryptoLink){
        if(!cryptoLink.upvoted){
            cryptoLink.upvoted = true;
            cryptoLink.upVoteCount = cryptoLink.upVoteCount + 1;
            $http.get('cryptoLink/' + cryptoLink.id + '/upvote')
                .then(
                    function (response) {
                        const serverData = response.data;
                        if (serverData.status != 200) {
                            alert(serverData.message);
                            cryptoLink.upVoteCount = cryptoLink.upVoteCount - 1;
                            return;
                        }
                    });
        }
    };

    $scope.downvote = function(cryptoLink){
        if(!cryptoLink.downvoted){
            cryptoLink.downvoted = true;
            cryptoLink.downVoteCount = cryptoLink.downVoteCount + 1;
            $http.get('cryptoLink/' + cryptoLink.id + '/downvote')
                .then(
                    function (response) {
                        const serverData = response.data;
                        if (serverData.status != 200) {
                            alert(serverData.message);
                            cryptoLink.downVoteCount = cryptoLink.downVoteCount - 1;
                            return;
                        }
                    });
        }
    };

    $scope.bookmark = function(cryptoLink){
        if(!cryptoLink.bookmarked){
            cryptoLink.bookmarked = true;
            cryptoLink.bookmarkCount = cryptoLink.bookmarkCount + 1;
            $http.get('cryptoLink/' + cryptoLink.id + '/bookmark')
                .then(
                    function (response) {
                        const serverData = response.data;
                        if (serverData.status != 200) {
                            alert(serverData.message);
                            cryptoLink.bookmarkCount = cryptoLink.bookmarkCount - 1;
                            return;
                        }
                    });
        }
    };

    $scope.showShareBtn = function(id){
        $("#"+id).toggle();
    };

    $scope.loadMore = function(){
        if($scope.data.links.currentPage === $scope.data.links.lastPage){
            $scope.loadMoreElements = false;
        }
        let nextPage = $scope.data.links.currentPage + 1;
        if($scope.loadMoreElements && $scope.startLoadingMoreElements) {
            $scope.startLoadingMoreElements = false;
            setTimeout(function(){
                $scope.startLoadingMoreElements = true;
                console.log('set load more to true');
            }, 8000);
            console.log("load more called....");
            $http.get('cryptoLink/loadmore?page=' + nextPage)
                .then(
                    function(response){
                        const serverData = response.data;
                        if(serverData.status != 200){
                            alert(serverData.message);
                            return;
                        }
                        if(serverData.result.links.content.length < 15){
                            $scope.loadMoreElements = false;
                        }
                        let id = $scope.data.links.content[$scope.data.links.content.length - 1].id;
                        serverData.result.links.content.forEach(link => {
                            $scope.data.links.content.push(link);
                        });
                        $scope.data.links.currentPage = nextPage;
                        $scope.data.links.lastPage = serverData.result.links.lastPage;
                        $scope.data.links.totalElements = serverData.result.links.totalElements;
                        setTimeout(function(){
                            document.getElementById('c' + id).scrollIntoView();
                        }, 800);
                    });
        }
    };

}]);

App.directive('onScrollToBottom', function ($document) {
    return {
        restrict: 'A',
        link: function (scope, element, attrs) {

            var doc = angular.element($document)[0].body;

            $document.bind("scroll", function () {
                /*if( doc.scrollTop === (doc.scrollHeight - doc.offsetHeight)) {
                    scope.$apply(attrs.onScrollToBottom);
                }*/
                /*if (doc.scrollTop + doc.offsetHeight >= doc.scrollHeight) {
                    scope.$apply(attrs.onScrollToBottom);
                }*/
                if( ((window.innerHeight + window.pageYOffset) >= document.body.offsetHeight - 1500)) {
                    scope.$apply(attrs.onScrollToBottom);
                }
            });
        }
    };
});