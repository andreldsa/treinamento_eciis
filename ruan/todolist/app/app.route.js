(function() {

    angular
        .module('todolistApp')
        .config(['$stateProvider', '$urlRouterProvider', routerConfig]);
    
    function routerConfig($stateProvider, $urlRouterProvider) {        
        
        $urlRouterProvider.otherwise('/home');        
        
        $stateProvider
            .state('home', {
                url: '/home',
                component: 'home'
            })
            .state('lists', {
                url: '/lists',
                component: 'lists'
            })
            .state('list-details', {
                url: '/list/{listId:int}',
                component: 'listDetails'
            })
            .state('list-form', {
                url: '/list',
                component: 'listForm'
            })
            .state('task-form', {
                url: '/list/{listId:int}/task/',
                component: 'taskForm'
            })
    }

})();