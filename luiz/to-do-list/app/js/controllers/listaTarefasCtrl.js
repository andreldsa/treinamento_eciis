
(function() {
    var app = angular.module('tarefasApp');

    app.controller('litaTarefasCtrl', function(todoService){
        vm = this;
        vm.tarefas = [];

        vm.buscarTodas = function() {
            todoService.buscarTodas().then(function(response) {
                vm.tarefas = response.data;

            }, function(response){
                console.log(response.data);
                window.location.replace(response.data.login_url);
            });
        };
    });
})();