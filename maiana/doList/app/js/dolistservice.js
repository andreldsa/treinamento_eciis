var service;

(function(){
    var app = angular.module('app');
    app.service('DoListService', function DoListService($http, $state){
        
        service = this;
        var _user;

        Object.defineProperties(service, {
                user: {
                    get: function () { return _user; },
                    set: function (data) { _user = data; }
                }
            })
        
        service.load = function() {
                $http.get('/api')
                .then(function sucess(response) {
                    _user = new User(response.data);
                }, function error(err) {
                    
                });
            }

        service.getList = function getList(){
            return $http.get('/api/list');
        }

        service.rgList = function rgList(list){
            return $http.post('/api/list', list);
        };

        service.removeList = function removeList(list){
            return $http.delete('/api/list/' + list);
        };
        service.getTask = function getTask(keyList){
            return $http.get('/api/'+keyList+'/list');
        };

        service.rgTask = function rgTask(keyList, activity){
            return $http.post('/api/'+keyList+'/list', activity);
        };

        service.updateTask = function updateTask(keyList, activity){
            return $http.put('/api/'+keyList+'/list', activity);
        };

        service.removeTask = function removeTask(keyList, keyTask){
            return $http.delete('/api/'+ keyList +'/' + keyTask);
        };
        
        // service initialization
        service.load();
    });
})();