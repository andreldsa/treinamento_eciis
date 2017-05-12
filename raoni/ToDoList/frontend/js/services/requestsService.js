/**
 * Created by raoni on 09/05/17.
 */


(function(){
angular.module('todoList').service('requestService', function($http){
    var service = this;

    service.fetchTasks = function () {
        return $http.get('http://localhost:8080/api/tasks');
    };

    service.putTask = function (data) {
            return $http.post('http://localhost:8080/api/tasks', data, {headers:{'Content-Type':'application/json'}});
    }

})

})();