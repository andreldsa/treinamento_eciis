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
            .state('list-details', {
                url: '/list/details',
                component: 'listDetails'
            })
            .state('tasks', {
                url: '/tasks',
                component: 'tasks'
            })
            .state('task-details', {
                url: '/task/details',
                component: 'taskDetails'
            })
    }

})();