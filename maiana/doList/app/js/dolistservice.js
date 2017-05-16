(function(){
    var app = angular.module('app');
    app.service('DoListService', function DoListService($http, $state){
        
    var sv = this;
    var _user;

    Object.defineProperties(sv, {
            user: {
                get: function () { return _user; },
                set: function (data) { _user = data; }
            }
        })
    
     sv.load = function() {
            $http.get('/api/user')
            .then(function sucess(response) {
                 _user = response.data;
            }, function error(err) {
                
            });
        }

    sv.getList = function getList(){
      return $http.get('/api');
    }

    sv.rgList = function rgList(activity){
        return $http.post('/api', activity);
    };

    sv.getTask = function getTask(idList){
        return $http.get('/api/'+idList+'/list');
    };

    sv.rgTask = function rgTask(idList, activity){
        return $http.post('/api/'+idList+'/list', activity);
    };
    
    // service initialization
    sv.load();
});
})();