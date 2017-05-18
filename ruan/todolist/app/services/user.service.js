(function() {

    angular
        .module('todolistApp')
        .service('UserService', ['$http', UserService]);

    function UserService($http) {
        var service = this;
        var _user;
        
        Object.defineProperties(service, {
            user: {
                get: function() { return _user; }
            }
        })

        service.load = function load() {
                $http.get('/api/users')
                    .then(function(response) {
                        if(typeof response.data != 'undefined'){
                            _user = new User(response.data);
                        } 
                    }, function(err) {
                        console.error(err.statusText);
                    });
        };

        service.load();
    }
})();