(function() {

    var app = angular.module('app', ['ui.router', 'ngMaterial']);

    app.config(function($stateProvider, $urlRouterProvider, $mdThemingProvider, $mdIconProvider){

        $mdIconProvider
            .iconSet();

        $urlRouterProvider.otherwise('/api');
        $stateProvider
            .state('app', {
                    'abstract': true,
                    'views': {
                        'header': {
                            templateUrl: "templates/header.html",
                            controller: "IndexController as vm",
                        }
                    }                
            })
            .state('app.login', {
                    url: "/login",
                    'views': {
                        'contents@': {
                            templateUrl: "templates/login.html",
                        }
                    }
            })
            .state('app.home', {
                    url: "/api",
                    'views': {
                        'contents@': {
                            templateUrl: "templates/home.html",
                            controller: "HomeController as vm",
                        }
                    }
            })
            .state('app.task', {
                    url: "/api/task",
                    params:{
                        'id' : '',
                        'name' : ''
                    },
                    'views': {
                        'contents@': {
                            templateUrl: "templates/tasks.html",
                            controller: "TaskController as vm",
                        }
                    }
            })
            .state('app.rgtask', {
                    url: "/rgtask",
                    'views': {
                        'contents@': {
                            templateUrl: "templates/register_task.html",
                            controller: "RgTaskController as vm",
                        }
                    }
            })
            .state('app.rglist', {
                    url: "/rglist",
                    'views': {
                        'contents@': {
                            templateUrl: "templates/register_list.html",
                            controller: "RgListController as vm",
                        }
                    }
            });
    });
    app.controller('IndexController', function IndexController(DoListService, $state){
        var vm = this;
        vm.ds = DoListService;

        Object.defineProperties(vm, {
                user: {
                    get: function () { return vm.ds.user; },
                    set: function (data) { vm.ds.user = data; }
                }
        });
        
        vm.stateGo = function stateGo(state){
            $state.go(state);
        }        
    });
})()
