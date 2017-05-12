
(function() {
    var app = angular.module('tarefasApp');
    app.service('taskService', function($http){
        var model = this;
        var TODO_URI = '/api/todo';

        model.buscarTodas = function() {
            return $http.get(TODO_URI);
        };

        model.salvar = function(tarefa) {
            return $http.post(TODO_URI, tarefa);
        };

        model.alertMessage = function() {
            window.alert('Faça login para poder realizar esta operação!')
        };
    });
})();