(function() {

    angular
        .module('todolistApp')
        .service('ListService', ['$http', ListService]);

    function ListService($http) {
        var url = 'http://localhost:8080/api/lists';
        var lists = [];
        
        $http.get(url).then(function(response) {
            lists = response.data;
        }, function errorCallback(response) {
            console.log(response);
        });

        this.getLists = function getLists() {
            return lists;
        };
    }
})();