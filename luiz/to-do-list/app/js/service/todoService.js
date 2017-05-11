
(function() {
    var app = angular.module('tarefasApp');
    app.service('todoService', function($http){
        var model = this;
        var TODO_URI = '/api/todo';
        var LOGIN_URL = '/login';
        var LOGOUT_URL = '/logout';

        model.buscarTodas = function() {
            return $http.get(TODO_URI);
        };

        model.salvar = function(tarefa) {
            return $http.post(TODO_URI, tarefa);
        };

        model.login = function() {
            window.location.replace(LOGIN_URL);
        };

        model.logout = function() {
            window.location.replace(LOGOUT_URL);
        };

        model.alertMessage = function() {
            window.alert('Faça login para poder realizar esta operação!')
        };
    });
})();