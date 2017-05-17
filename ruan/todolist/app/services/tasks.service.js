(function() {

    angular
        .module('todolistApp')
        .service('TaskService', ['$http', TaskService]);

    function TaskService($http) {
        var service = this;

        service.getTasksFromList = function getTasksFromList(listId) {
            return $http.get('/api/lists/'+ listId +'/tasks');
        };


        service.getTask = function getTask(listId, taskId) {
            return $http.get('/api/lists/' + listId + '/tasks/' + taskId);
        };


         service.deleteTask = function deleteTask(taskId) {
            console.log("deleted: " + taskId);
        }


        service.save = function save(listId, task, callback) {
            var url = '/api/lists/' + listId + '/task';

            $http.post(url, task)
                .then(function success(response) {
                    callback(response)
                }, function error(response) {
                    console.log(response)
                });
        }
    }
})();