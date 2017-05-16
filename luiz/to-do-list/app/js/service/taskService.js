(function() {
    var app = angular.module('tarefasApp');
    app.service('taskService', function($http){
        var model = this;
        var TODO_URI = '/api/todo';
        var _user;
        Object.defineProperties(model, {
            user: {
                get: function() {return _user},
                set: function(data) {_user = data}
            },
        });

        model.buscarTodas = function() {
            return $http.get(TODO_URI);
        };

        model.salvar = function(tarefa) {
            return $http.post(TODO_URI, tarefa);
        };

        var load = function() {
            $http.get('/api').then(function(response){
                _user = response.data;
            }, function(response) {});
        };

        load();
    });
})();