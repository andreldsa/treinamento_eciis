/**
 * Created by raoni on 09/05/17.
 */

var vm;
(function(){
angular.module('todoList').service('requestService', function($http){
    vm = this;
    vm.fetchTasks = function () {
        $http.get('http://localhost:8080/api/tasks',{headers:{'content-type':'application/json'}})
            .then(function (response) {
        return response.data;
        });
    };

    vm.putTasks = function (data) {
        $http.post('http://localhost:8080/api/tasks', data);
    }

})

})();