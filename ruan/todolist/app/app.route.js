(function() {

    angular
        .module('todolistApp')
        .config(routerConfig);
    
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
                url: '/list/details',
                component: 'listDetails'
            })
            .state('list-form', {
                url: '/list/new',
                component: 'listForm'
            })
            .state('task-form', {
                url: '/task/new',
                component: 'taskForm'
            })
    }

})();