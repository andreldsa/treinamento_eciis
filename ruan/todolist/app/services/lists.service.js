(function() {

    angular
        .module('todolistApp')
        .service('ListService', ['$http', ListService]);

    function ListService($http) {
        var service = this;
        var _lists = [];

        Object.defineProperties(service, {
            lists: {
                get: function() { return _lists; }
            }
        })        

        service.getLists = function getLists() {
            $http.get('/api/lists')
                .then(function(response) {
                    _lists = response.data;
                }, function(err) {
                    console.error(err);
                });
        };


        service.getList = function getList(listId) {
            return $http.get('/api/lists/'+ listId);
        }


        service.deleteList = function deleteList(listId) {
            console.log("deleted: " + listId);
        }


        service.save = function save(newList) {
            $http.post('/api/list', newList)
                .then(function(response) {
                    console.log(response);
                }, function(err) {
                    console.error(err);
                });
        }


        service.getLists();
    }
})();