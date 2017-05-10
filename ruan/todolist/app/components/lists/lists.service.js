(function() {

    angular
        .module('todolistApp')
        .service('ListService', ['$http', ListService]);

    function ListService($http) {
        var url = 'http://localhost:8080/api/';
        var lists = [];
        

        this.getAll = function getAll() {
            var getUrl = url + 'lists';

            $http.get(getUrl).then(function success(response) {
                lists = response.data;
            }, function errorCallback(response) {
                console.log(response);
            });

            return lists;
        };

        this.save = function save(newList) {
            var postUrl = url + 'list';

            $http.post(postUrl, newList)
                .then(function success(response) {
                    console.log(response);
                }, function errorCallback(response) {
                    console.log(response);
                });
        }
    }
})();