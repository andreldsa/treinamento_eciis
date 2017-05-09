
(function() {
    var app = angular.module('tarefasApp');

    app.controller('tarefasController', function($http, todoService) {
        vm = this;

        vm.salvar = function(tarefa) {
            todoService.salvar(tarefa).then(function(response) {
                vm.tarefa = "";

            }, function(response){});
        };
    });
})();