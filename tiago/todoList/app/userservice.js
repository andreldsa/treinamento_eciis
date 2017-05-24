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
        });

        service.load = function() {
            $http.get('/api')
            .then(function (response) {
                // ok
                if (typeof response.data.user != 'undefined') {
                    _user = new User();
                } else {
                    _user = {}
                }
                _user.tasks = response.data.tasks;
                _user.email = response.data.email;
            }, function (err) {
                // err
            });
        };

        service.save = function(operation, task) {
            _user._state = 'saving';
            task.operation = operation;
            var promise = $http.put(
                '/api/update/' + _user.email, JSON.stringify(task)
            ).then(function (response) {
                if(operation == 'add') {
                    _user.add_task(response.data);
                } else {
                    _user.del_task(task.id);
                };
                _user._state = 'saved';
            }, function (err) {
                alert('Não foi possível salvar os dados!');
                _user._state = 'changed';
            });
            return promise;
        };
        // service initialization
        service.load(); 
    });
})();