var vm;

(function() {
    var app = angular.module('tarefasApp', ['ngMaterial', 'ui.router']);

    app.config(function($mdThemingProvider, $mdIconProvider, $stateProvider, $urlRouterProvider) {
        setupMaterialDesign($mdThemingProvider, $mdIconProvider);

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

    function setupMaterialDesign($mdThemingProvider, $mdIconProvider) {
        $mdThemingProvider.theme('dark-grey').backgroundPalette('grey').dark();
        $mdThemingProvider.theme('dark-orange').backgroundPalette('orange').dark();
        $mdThemingProvider.theme('dark-purple').backgroundPalette('deep-purple').dark();
        $mdThemingProvider.theme('dark-blue').backgroundPalette('blue').dark();
        $mdThemingProvider.theme('docs-dark');

        $mdIconProvider
            .iconSet("call", 'img/icons/sets/communication-icons.svg', 24)
            .iconSet("social", 'img/icons/sets/social-icons.svg', 24);

    };
})();