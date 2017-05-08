
(function() {

    var app = angular.module('tarefasApp')

    app.controller('litaTarefasCtrl', function(todoService){

        vm = this;

        vm.tarefas = []

        vm.buscarTodas = function() {
            todoService.buscarTodas().then(function(response) {

                console.log(response.status);
                console.log(response.data);

                vm.tarefas = response.data

            }, function(response){})
        }
    })
})()