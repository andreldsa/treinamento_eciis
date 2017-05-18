(function() {

    angular
        .module('todolistApp')
        .service('UserService', ['$http', UserService]);

    function UserService($http) {
        var service = this;

        service.getUserData = function getUserData(listId) {
            return $http.get('/api/users')
        };
    }
})();