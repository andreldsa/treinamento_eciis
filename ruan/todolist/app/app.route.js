(function() {

    angular
        .module('todolistApp')
        .config(routerConfig);
    
    function routerConfig($stateProvider, $urlRouterProvider) {        
        
        $urlRouterProvider.otherwise('/lists');        
        
        $stateProvider
            .state('about', {
                url: '/about',
                component: 'about'
            })
            .state('lists', {
                url: '/lists',
                component: 'lists'
            })
            .state('tasks', {
                url: '/tasks',
                component: 'tasks'
            })
            .state('list-details', {
                url: '/list/details',
                component: 'listDetails'
            })
            .state('task-details', {
                url: '/task/details',
                component: 'taskDetails'
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