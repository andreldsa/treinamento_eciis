(function () {
    var app = angular.module('tarefasApp');

    app.controller('tarefasController', function($http, taskService) {
        vm = this;
        vm.createdTasks = [];
        vm.tasks = [];
        vm.enableProgress;

        vm.salvar = function(tarefa) {
            taskService.salvar(tarefa).then(function(response) {
                vm.tarefa = "";
                vm.createdTasks.push(response.data);

            }, function(response) {
            });
        };

        var load = function() {
            vm.enableProgress = true;
            
            taskService.buscarTodas().then(function(response) {
                vm.enableProgress = false;
                vm.tasks= response.data;

            }, function(response) {
            });
        };

        load();
    });
})();