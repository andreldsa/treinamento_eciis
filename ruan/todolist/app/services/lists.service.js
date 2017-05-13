(function() {

    angular
        .module('todolistApp')
        .service('ListService', ['$http', ListService]);

    function ListService($http) {
        var service = this;
        
        service.getAll = function getAll() {
            return  $http.get('/api/lists');
        };


        service.getOne = function getOne(listId) {
            return $http.get('/api/list/'+ listId);
        }


        service.deleteOne = function deleteOne(listId) {
            console.log("deleted: " + listId);
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