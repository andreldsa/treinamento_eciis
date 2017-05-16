/**
 * Created by raoni on 08/05/17.
 */
(function(){
    angular
        .module('todoList', ['ngMaterial', 'ui.router'])
        .config(function($urlRouterProvider, $stateProvider){
            $urlRouterProvider.otherwise('/');

            $stateProvider
                .state('view_tasks', {
                    url: '/view/tasks',
                    templateUrl: 'templates/tasks.html',
                    controller: 'taskController as vm'
                })
                .state('post_tasks', {
                    url: '/post/tasks',
                    templateUrl: 'templates/postasks.html',
                    controller: 'taskController as vm'
                })
                .state('home', {
                    url: '/'
                });
        });
})();