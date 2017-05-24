"use strict";
(function() {
  var app = angular.module('app', ['ngMaterial', 'ui.router']);
  
  app.config(function($mdIconProvider, $urlRouterProvider, $stateProvider) {
    $mdIconProvider.fontSet('md', 'material-icons');
    // configurações de states
    $urlRouterProvider.otherwise('/');
    $stateProvider
    .state('app', {
        'abstract': true,
        'views': {
            'header': {
                templateUrl: 'header.html'
            }
        }
    })
    .state('app.about', {
        'url': '/about',
        'views': {
            'about@': {
                templateUrl: 'about.html'
            },
        }
    })
    .state('app.home', {
        'url': '/',
        'views': {
            'contents@': {
                templateUrl: 'home.html',
                controller: 'TasksCtrl as vm'
            },
        }
    })
    .state('app.tasksRegister', {
        'url': '/ct',
        'views': {
            'contents@': {
                templateUrl: 'tasksRegister.html',
                controller: 'TasksCtrl as vm'
            },
        }
    })
  });

  app.controller('AppCtrl', function AppCtrl(UserService) {
        var vm = this;
        Object.defineProperties(vm, {
            user: {
                get: function () { return UserService.user; },
                set: function (data) { UserService.user = data; }
            }
        });
    });
})();