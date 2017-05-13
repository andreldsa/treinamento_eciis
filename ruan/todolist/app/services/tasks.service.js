(function() {

    angular
        .module('todolistApp')
        .service('TaskService', ['$http', TaskService]);

    function TaskService($http) {
        var service = this;

        service.getAll = function getAll() {
            return $http.get('/api/tasks');
        };


        service.getOne = function getOne(taskId) {i
            return $http.get('/api/task/' + taskId);
        };


        service.getAllFromList = function getAllFromList(listId) {
            return $http.get('/api/list/' + listId + '/tasks');
        };


         service.deleteOne = function deleteOne(taskId) {
            console.log("deleted: " + taskId);
        }


        service.save = function save(listId, task) {
            var url = '/api/list/' + listId + '/task';

            $http.post(url, task)
                .then(function success(response) {
                    console.log(response)
                }, function errorCallback(response) {
                    console.log(response)
                });
        }
    }
})();