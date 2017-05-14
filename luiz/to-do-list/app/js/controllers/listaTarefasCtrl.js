
(function() {
    var app = angular.module('tarefasApp');

    app.controller('litaTarefasCtrl', function(taskService){
        vm = this;
        vm.tarefas = [];

        vm.buscarTodas = function() {
            taskService.buscarTodas().then(function(response) {
                taskService.enableProgress = false;
                vm.tarefas = response.data;

            }, function(response){
                if(response.status == 401) {
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