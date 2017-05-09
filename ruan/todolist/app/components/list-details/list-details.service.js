(function() {

    angular
        .module('todolistApp')
        .service('ListDetailsService', ['$http', ListDetailsService]);

    function ListDetailsService($http) {
        var url = 'http://localhost:8080/api/list';
        var list = null;
        
        $http.get(url).then(function(response) {
            list = response.data;
        }, function errorCallback(response) {
            console.log(response);
        });

        this.getList = function getList() {
            return list;
        };
    }
})();