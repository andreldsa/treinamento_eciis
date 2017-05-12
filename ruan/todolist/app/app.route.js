(function() {

    angular
        .module('todolistApp')
        .config(['$stateProvider', '$urlRouterProvider', routerConfig]);
    
    function routerConfig($stateProvider, $urlRouterProvider) {        
        
        $urlRouterProvider.otherwise('/lists');        
        
        $stateProvider
            .state('lists', {
                url: '/lists',
                component: 'lists'
            })
            .state('task-card', {
                url: '/taskCard',
                component: 'taskCard'
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