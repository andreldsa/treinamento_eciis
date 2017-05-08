(function() {

    angular
        .module('todolistApp')
        .service('TaskService', ['$http', TaskService]);

    function TaskService($http) {
        var url = 'http://localhost:8080/api/tasks';
        var tasks = [];

        $http.get(url).then(function(response) {
            tasks = response.data;
        }, function errorCallback(response) {
            console.log(response);
        });

        this.getTasks = function getTasks() {
            return tasks;
        }
    }
})();