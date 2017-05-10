(function() {

    angular
        .module('todolistApp')
        .service('TaskService', ['$http', TaskService]);

    function TaskService($http) {
        var url = 'http://localhost:8080/api/';
        var tasks = [];

        this.getAll = function getAll() {
            var getUrl = url + 'tasks'
                
            $http.get(getUrl).then(function(response) {
                tasks = response.data;
            }, function errorCallback(response) {
                console.log(response);
            });

            return tasks;
        };

        this.save = function save(newTask) {
            var listId = 5066549580791808;
            var postUrl = url + 'list/' + listId + '/task';

            $http.post(postUrl, newTask)
                .then(function success(response) {
                    console.log(response)
                }, function errorCallback(response) {
                    console.log(response)
                });
        }
    }
})();