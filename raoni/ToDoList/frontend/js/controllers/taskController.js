/**
 * Created by raoni on 08/05/17.
 */
var vm;
(function() {

    angular.module('todoList').controller('taskController', ['$http', function ($http) {
        vm = this;
        vm.tasks = [];

        vm.fetchTasks = function () {
            $http.get('http://localhost:8080/api/tasks',{headers:{'content-type':'application/json'}}).then(function (response) {
                console.log("entrou");
                vm.tasks = response.data;
            });
        };
    }]);

})();
