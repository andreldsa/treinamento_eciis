
(function() {
    var app = angular.module('tarefasApp')
    app.service('todoService', function($http){
        var model = this;

        model.buscarTodas = function() {
            return $http.get('/api/todo')
        }

        model.salvar = function(tarefa) {
            return $http.post('/api/todo', tarefa)
        }
    });
})()