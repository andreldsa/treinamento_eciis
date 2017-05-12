(function() {

    angular
        .module('todolistApp')
        .service('TaskService', ['$http', TaskService]);

    function TaskService($http) {
        var service = this;
        var tasks;

        service.getAll = function getAll() {
            return $http.get('/api/tasks');
        };

        service.save = function save(task, listId) {
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