
(function() {
    var app = angular.module('tarefasApp');
    app.service('todoService', function($http){
        var model = this;
        var TODO_URI = '/api/todo';

        model.buscarTodas = function() {
            return $http.get(TODO_URI);
        };

        model.salvar = function(tarefa) {
            return $http.post(TODO_URI, tarefa);
        };

        model.login = function() {
            window.location.replace('/api/login');
        };

        model.logout = function() {
            window.location.replace('/api/logout');
        };

        model.alertMessage = function() {
            window.alert('Faça login para poder realizar esta operação!')
        };
    });
})();