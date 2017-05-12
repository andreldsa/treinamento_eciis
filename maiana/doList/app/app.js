(function() {

var app = angular.module('app', ['ui.router', 'ngMaterial']);

app.config(function($stateProvider, $urlRouterProvider, $mdThemingProvider, $mdIconProvider){

    $mdIconProvider
        .iconSet();

    $urlRouterProvider.otherwise('/api');

    $stateProvider
        .state("login", {
                url: "/login",
                templateUrl: "templates/login.html",
        }).state("home", {
                url: "/api",
                templateUrl: "templates/home.html",
                controller: "HomeController",
        })
        .state("register", {
                url: "/register",
                templateUrl: "templates/register.html",
                controller: "RegisterController",
        });

});

app.controller('IndexController', function IndexController(DoListService, $state){
    var vm = this;
    vm.tasks = {};
    vm.logged_in = DoListService.logged_in;
    
    vm.stateGo = function stateGo(state){
        $state.go(state);
    }
        
});

app.controller('HomeController', function HomeController(DoListService, $state){
    var vm = this;
    vm.tasks = {}

    DoListService.getList().then(
            function sucess(response){
                vm.tasks = response.data;
            }, function error(response){
                if(response.status == 401) {
                    vm.stateGo('login');
                }
            }
        );
    
    vm.stateGo = function stateGo(state){
        $state.go(state);
    }
        
});

app.controller('RegisterController', function RegisterController(DoListService, $state){    
    var vm = this;
    vm.activity = {}

    vm.register = function register(){
        DoListService.register(vm.activity).then(
            function sucess(response){
                vm.activity = {};
                vm.stateGo('home');
                return response.data;
        }, function error(response){
             if(response.status == 401) {
                   vm.stateGo('login');
                }
        });
    }; 

    vm.stateGo = function stateGo(state){
        $state.go(state);
    }
    
});

app.service('DoListService', function DoListService($http, $state){

    var sv = this;

    sv.getList = function getList(){
      return $http.get('/api');
    }

    sv.register = function register(activity){
        return $http.post('/api', activity);

    };
});
})()
