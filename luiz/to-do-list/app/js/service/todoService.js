
(function() {
    var app = angular.module('tarefasApp')
    app.service('todoService', function($http){
        var model = this;

        var TODO_URI = '/api/todo';

        model.buscarTodas = function() {
            return $http.get(TODO_URI);
        }

        model.salvar = function(tarefa) {
            return $http.post(TODO_URI, tarefa);
        }
    });
})()