(function(){
angular.module('todoList').service('requestService', function($http){
    var service = this;
    var _user;
    Object.defineProperties(service, {
        user: {
            get: function () { return _user; },
            set: function (data) { _user = data; }
        }
    })

    service.fetchTasks = function () {
        return $http.get('/api/tasks');
    };

    service.login = function (){
        window.location.replace('/api/login');
    };

    service.putTask = function (data) {
        return $http.post('/api/tasks', data);
    };

    service.deleteTasks = function(id) {
        return $http.delete('/api/delete/' + id);
    };
})})();