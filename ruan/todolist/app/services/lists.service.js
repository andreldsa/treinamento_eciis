(function() {

    angular
        .module('todolistApp')
        .service('ListService', ['$http', ListService]);

    function ListService($http) {
        var service = this;
        

        service.getLists = function getLists() {
            return  $http.get('/api/lists');
        };


        service.getList = function getList(listId) {
            return $http.get('/api/lists/'+ listId);
        }


        service.deleteList = function deleteList(listId) {
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