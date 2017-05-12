var vm;

(function() {
    var app = angular.module('tarefasApp', ['ngMaterial', 'ui.router']);

    app.config(function($mdIconProvider, $stateProvider, $urlRouterProvider) {
        setupMaterialDesign($mdIconProvider);

        $urlRouterProvider.otherwise('/tarefa');

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
            });
    });

    function setupMaterialDesign($mdIconProvider) {
        $mdIconProvider
            .iconSet("call", 'img/icons/sets/communication-icons.svg', 24)
            .iconSet("social", 'img/icons/sets/social-icons.svg', 24);
    };
})();