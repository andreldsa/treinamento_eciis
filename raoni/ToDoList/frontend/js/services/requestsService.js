/**
 * Created by raoni on 09/05/17.
 */


(function(){
angular.module('todoList').service('requestService', function($http){
    var service = this;

    service.fetchTasks = function () {
        return $http.get('/api/tasks');
    };

    service.login = function (){
        window.location.replace('/api/login');
    };

    service.putTask = function (data) {
        return $http.post('/api/tasks', data);

    };

    service.deleteTasks = function(name) {
        return $http.delete('/api/delete/' + name);
    };
})})();