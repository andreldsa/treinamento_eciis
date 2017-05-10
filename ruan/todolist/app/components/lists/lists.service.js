(function() {

    angular
        .module('todolistApp')
        .service('ListService', ['$http', ListService]);

    function ListService($http) {
        var url = 'http://localhost:8080/api/';
        var lists = [];
        

        this.getLists = function getLists() {
            
            $http.get(url + 'lists').then(function(response) {
                lists = response.data;
            }, function errorCallback(response) {
                console.log(response);
            });

            return lists;
        };

        this.saveList = function saveList(newList) {

        }
    }
})();