
(function() {

    var app = angular.module('tarefasApp')

    app.controller('tarefasController', function($http, todoService) {

        vm = this;

        vm.salvar = function(tarefa) {
            todoService.salvar(tarefa).then(function(response) {
                delete vm.tarefa
                console.log(response.status);
                console.log(response.data);

            }, function(response){})
        }
    });
})()