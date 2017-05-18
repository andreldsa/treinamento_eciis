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

        vm.deletar = function(task_id) {
            console.log(task_id);
            vm.createdTasks.splice(-1,1);
            taskService.deletar(task_id).then(function(response) {
                //success
                var index = vm.tasks.indexOf(response.data);
                vm.tasks.splice(index,1);

                index = vm.createdTasks.indexOf(response.data);
                vm.createdTasks.splice(index,1);
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