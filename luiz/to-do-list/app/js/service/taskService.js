(function() {
    var app = angular.module('tarefasApp');
    app.service('taskService', function($http){
        var model = this;
        var TODO_URI = '/api/todo';
        var _user;
        var _enableProgress = false;
        Object.defineProperties(model, {
            user: {
                get: function() {return _user},
                set: function(data) {_user = data}
            },
            enableProgress: {
                get: function() {return _enableProgress},
                set: function(data) {_enableProgress = data}
            }
        });

        model.buscarTodas = function() {
            return $http.get(TODO_URI);
        };

        model.salvar = function(tarefa) {
            return $http.post(TODO_URI, tarefa);
        };

        model.alertMessage = function() {
            window.alert('Faça login para poder realizar esta operação!');
        };

        var load = function() {
            $http.get('/api').then(function(response){
                _user = response.data;
            }, function(response) {});
        };

        load();
    });
})();