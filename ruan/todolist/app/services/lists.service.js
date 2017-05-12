(function() {

    angular
        .module('todolistApp')
        .service('ListService', ['$http', ListService]);

    function ListService($http) {
        var service = this;
        
        service.getAll = function getAll() {
            return  $http.get('/api/lists');
        };


        service.getOne = function getOne(id) {
            return $http.get('/api/list/'+ id);
        }


        service.save = function save(newList) {
            $http.post('/api/list', newList)
                .then(function success(response) {
                    console.log(response);
                }, function errorCallback(response) {
                    console.log(response);
                });
        }
    }
})();