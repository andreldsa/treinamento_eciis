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
                        templateUrl: 'partial/header.html',
                        controller: 'sideNavCtrl as vm'
                    }
                }
            })
            .state('app.adicionar-tarefa', {
                url: '/',
                views: {
                    'contents@': {
                        templateUrl: 'partial/adicionar-tarefa.html',
                        controller: 'tarefasController as vm'
                    }
                }
            })
            .state('app.tarefas', {
                url: '/todas-tarefas',
                views: {
                    'contents@': {
                        templateUrl: 'partial/visualizar-tarefas.html',
                        controller: 'tarefasController as vm'
                    }
                }
            });
    });
})();