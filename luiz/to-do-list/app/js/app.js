var vm;

(function() {
    var app = angular.module('tarefasApp', ['ngMaterial', 'ui.router']);

    app.config(function($stateProvider, $urlRouterProvider) {
        $urlRouterProvider.otherwise('/');

        $stateProvider
            .state('app', {
                abstract: true,
                views: {
                    'header': {
                        templateUrl: 'header.html',
                        controller: 'sideNavCtrl as vm'
                    }
                }
            })
            .state('app.adicionar-tarefa', {
                url: '/',
                views: {
                    'contents@': {
                        templateUrl: 'adicionar-tarefa.html',
                        controller: 'tarefasController as vm'
                    }
                }
            })
            .state('app.tarefas', {
                url: '/todas-tarefas',
                views: {
                    'contents@': {
                        templateUrl: 'visualizar-tarefas.html',
                        controller: 'litaTarefasCtrl as vm'
                    }
                }
            });
    });
})();