var vm;

(function() {
    var app = angular.module('tarefasApp', ['ngMaterial', 'ui.router'])
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

    app.service('todoService', function($http){

        var model = this;

        model.buscarTodas = function() {
            return $http.get('http://' + location.host + '/api/todo')
        }

        model.salvar = function(tarefa) {
            return $http.post('http://' + location.host + '/api/todo', tarefa)
        }
    });

    app.config(function($mdThemingProvider, $stateProvider, $urlRouterProvider) {
        $mdThemingProvider.theme('dark-grey').backgroundPalette('grey').dark();
        $mdThemingProvider.theme('dark-orange').backgroundPalette('orange').dark();
        $mdThemingProvider.theme('dark-purple').backgroundPalette('deep-purple').dark();
        $mdThemingProvider.theme('dark-blue').backgroundPalette('blue').dark();
        $mdThemingProvider.theme('docs-dark');

        $urlRouterProvider.otherwise('/tarefa')

        $stateProvider

            .state('adicionar-tarefa', {
                url: '/tarefa',
                templateUrl: 'adicionar-tarefa.html',
                controller: 'tarefasController as vm'
            })

            .state('tarefas', {
                url: '/todas-tarefas',
                templateUrl: 'visualizar-tarefas.html',
                controller: 'litaTarefasCtrl as vm'
            })
    });

})()