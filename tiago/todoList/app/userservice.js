(function () {
    var app = angular.module('app');
    
    app.service('UserService', function UserService($http, $q) {
        var service = this;
        var _user;
        Object.defineProperties(service, {
            user: {
                get: function () { return _user; },
                set: function (data) { _user = data; }
            }
        })

        service.load = function() {
            $http.get('/api')
            .then(function (response) {
                // ok
                if (typeof response.data.usuario != 'undefined') {
                    _user = new Usuario(response.data.usuario);
                } else {
                    _user = {}
                }
                _user.email = response.data.email;
            }, function (err) {
                // err
            });
        }

        service.save = function() {
            _user._state = 'saving';
            var promise = $http({
                method: 'PUT',
                url: '/api/usuario/' + _user.email,
                data: JSON.stringify(_user)
            }).then(function (response) {
                _user._state = 'saved';
            }, function (err) {
                alert('Não foi possível salvar os dados!');
                _user._state = 'changed';
            })
            return promise;
        }
        // service initialization
        service.load(); 
    });
})();