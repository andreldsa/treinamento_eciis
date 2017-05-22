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


         service.deleteTask = function deleteTask(listId, taskId) {
            return $http.delete('/api/lists/' + listId + '/tasks/' + taskId);
        }


        service.save = function save(listId, task) {
            var url = '/api/lists/' + listId + '/task';
            var promise = $http.post(url, task)
                            .then(function(response) {
                                console.log(response);                            
                            }, function(err) {
                                console.error(err);
                            });

            return promise;
        }
    }
})();