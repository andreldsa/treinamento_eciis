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
                        controller: "IndexController",
                    }
                }                
        }).state('app.login', {
                url: "/login",
                'views': {
                    'contents@': {
                        templateUrl: "templates/login.html",
                    }
                }
        }).state('app.home', {
                url: "/api",
                'views': {
                    'contents@': {
                        templateUrl: "templates/home.html",
                        controller: "HomeController",
                    }
                }
        }).state('app.task', {
                url: "/api/task",
                params:{
                    'id' : ''
                },
                'views': {
                    'contents@': {
                        templateUrl: "templates/tasks.html",
                        controller: "TaskController",
                    }
                }
        })
        .state('app.rgtask', {
                url: "/rgtask",
                'views': {
                    'contents@': {
                        templateUrl: "templates/register_task.html",
                        controller: "RgTaskController",
                    }
                }
        }).state('app.rglist', {
                url: "/rglist",
                'views': {
                    'contents@': {
                        templateUrl: "templates/register_list.html",
                        controller: "RgListController",
                    }
                }
        });

});

app.controller('IndexController', function IndexController(DoListService, $state){
    var vm = this;
    
    Object.defineProperties(vm, {
            user: {
                get: function () { return DoListService.user; },
                set: function (data) { DoListService.user = data; }
            }
        })
    
    vm.stateGo = function stateGo(state){
        $state.go(state);
    }
        
});

app.controller('HomeController', function HomeController(DoListService, $state){
    var vm = this;
    vm.lists = {}

    DoListService.getList().then(
            function sucess(response){
                vm.lists = response.data;
            }, function error(response){
                if(response.status == 401) {
                    vm.stateGo('app.login');
                }
            }
        );
    
    vm.stateGo = function stateGo(state){
        $state.go(state);
    };

     vm.goTasks = function goTasks(idList){
         $state.go('app.task', { 'id': idList });  
    }
        
});

app.controller('TaskController', function TaskController(DoListService, $state, $stateParams){
    var vm = this;
    vm.tasks = {};
    vm.list= $stateParams.id;

    DoListService.getTask(vm.list).then(
            function sucess(response){
                vm.tasks = response.data;

            }, function error(response){
                if(response.status == 401) {
                    vm.stateGo('app.login');
                }
            }
        );      
});

app.controller('RgTaskController', function RegisterController(DoListService, $state){    
    var vm = this;
    vm.activity = {};
    vm.list = {
        'name' : ""
    };

    vm.register = function register(){
        DoListService.rgTask(vm.list.name, vm.activity).then(
            function sucess(response){
                vm.activity = {};
                vm.list = {
                    'name' : ""
                };

                return response.data;
        }, function error(response){
             if(response.status == 401) {
                   vm.stateGo('app.login');
                }
        });
    }; 

    vm.stateGo = function stateGo(state){
        $state.go(state);
    }
    
});

app.controller('RgListController', function RegisterController(DoListService, $state){    
    var vm = this;
    vm.list = {}

    vm.register = function register(){
        DoListService.rgList(vm.activity).then(
            function sucess(response){
                vm.activity = {};
                return response.data;
        }, function error(response){
             if(response.status == 401) {
                   vm.stateGo('app.login');
                }
        });
    }; 

    vm.stateGo = function stateGo(state){
        $state.go(state);
    }
    
});

app.service('DoListService', function DoListService($http, $state){

    var sv = this;
    var _user;

    Object.defineProperties(sv, {
            user: {
                get: function () { return _user; },
                set: function (data) { _user = data; }
            }
        })
    
     sv.load = function() {
            $http.get('/api/user')
            .then(function sucess(response) {
                 _user = true;
            }, function error(err) {
                _user = false;
            });
        }

    sv.getList = function getList(){
      return $http.get('/api');
    }

    sv.rgList = function rgList(activity){
        return $http.post('/api', activity);
    };

    sv.getTask = function getTask(idList){
        return $http.get('/api/'+idList+'/list');
    };

    sv.rgTask = function rgTask(idList, activity){
        return $http.post('/api/'+idList+'/list', activity);
    };
    
    // service initialization
    sv.load();
});
})()
