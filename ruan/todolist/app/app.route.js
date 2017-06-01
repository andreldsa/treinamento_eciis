(function() {

    angular
        .module('todolistApp')
        .config(routerConfig);
    
    function routerConfig($stateProvider, $urlRouterProvider) {        
        
        $urlRouterProvider.otherwise('/lists');        
        
        $stateProvider
            .state('about', {
                url: '/about',
                templateUrl: 'components/about/about.html',
                controller: 'AboutController as vm'
            })
            .state('lists', {
                url: '/lists',
                templateUrl: 'components/lists/lists.html',
                controller: 'ListsController as vm'
            })
            .state('tasks', {
                url: '/tasks',
                templateUrl: 'components/tasks/tasks.html',
                controller: 'TasksController as vm'
            })

    }

})();