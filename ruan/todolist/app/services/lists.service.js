(function () {

    angular
        .module('todolistApp')
        .service('ListService', ['$http', ListService]);

    function ListService($http) {
        var service = this;
        var _lists = [];

        Object.defineProperties(service, {
            lists: {
                get: function () { return _lists; }
            }
        })


        service.getLists = function getLists() {
            $http.get('/api/lists')
                .then(function (response) {
                    dataCollection = response.data;
                    _lists = _.map(dataCollection, function (data) {
                        return new List(data);
                    });
                }, function (err) {
                    console.error(err);
                });
        };


        service.getList = function getList(listId) {
            return $http.get('/api/lists/' + listId);
        }


        service.deleteList = function deleteList(listId) {
            $http.delete('/api/lists/' + listId)
                .then(function (response) {
                    _.remove(service.lists, function (list) {
                        return list.id == listId;
                    });
                });
        }


        service.updateList = function updateList(listId, list) {
            console.log('update list');
            // TODO create method on backend
        }


        service.save = function save(newList) {
            $http.post('/api/list', newList)
                .then(function (response) {
                    service.lists.push(response.data);
                }, function (err) {
                    console.error(err);
                });
        }


        service.getLists();
    }
})();