
(function() {
    var app = angular.module('tarefasApp');

    app.controller('litaTarefasCtrl', function(taskService){
        vm = this;
        vm.tarefas = [];

        vm.buscarTodas = function() {
            taskService.buscarTodas().then(function(response) {
                vm.tarefas = response.data;

            }, function(response){
                if(response.status == 401) {
                    taskService.alertMessage();
                }
            });
        };
        vm.buscarTodas();
    });
})();