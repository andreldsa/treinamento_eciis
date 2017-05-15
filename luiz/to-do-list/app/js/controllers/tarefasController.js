(function () {
    var app = angular.module('tarefasApp');

    app.controller('tarefasController', function($http, taskService) {
        vm = this;
        vm.createdTasks = [];
        vm.tasks = [];

        vm.salvar = function(tarefa) {
            taskService.salvar(tarefa).then(function(response) {
                vm.tarefa = "";
                vm.createdTasks.push(response.data);

            }, function(response) {
                if (response.status == 401) {
                    taskService.alertMessage();
                }
            });
        };

        vm.buscarTodas = function() {
            taskService.buscarTodas().then(function(response) {
                taskService.enableProgress = false;
                vm.tasks= response.data;

            }, function(response) {
                if (response.status == 401) {
                    taskService.alertMessage();
                }
            });
        };

        vm.load = function() {
            taskService.enableProgress = true;
        };

        vm.load();
        vm.buscarTodas();
    });
})();