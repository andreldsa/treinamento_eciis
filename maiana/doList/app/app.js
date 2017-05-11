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
                controller: "LoginController",
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

app.controller('IndexController', function IndexController(DoListService){
    var vm = this;
    vm.tasks = {}

    vm.login = function login(){
        DoListService.login();
    }

    vm.logout = function logout(){
        DoListService.logout();
        DoListService.stateGo('login');
    }
    
    vm.stateGo = function stateGo(state){
        DoListService.stateGo(state);
    }
        
});

app.controller('HomeController', function HomeController(DoListService){
    var vm = this;
    vm.tasks = {}

    DoListService.getList().then(
            function sucess(response){
                vm.tasks = response.data;
            }, function error(response){}
        );
    
    vm.stateGo = function stateGo(state){
        DoListService.stateGo(state);
    }
        
});

app.controller('RegisterController', function RegisterController(DoListService){    
    var vm = this;
    vm.activity = {}

    vm.register = function register(){
        DoListService.register(vm.activity).then(
            function sucess(response){
                vm.activity = {};
                // vm.ActivityForm.$setPristine(); Tornar o campo pristine novamente
                return response.data;
        }, function error(response){

        });
    }; 

    vm.stateGo = function stateGo(state){
        DoListService.stateGo(state);
    }
    
});

app.controller('LoginController', function LoginController(DoListService){
    var vm = this;
    vm.tasks = {}

    vm.login = function login(){
        DoListService.login();
    };
        
});

app.service('DoListService', function DoListService($http, $state){

    var sv = this;
    sv.getList = function getList(){
      return $http.get('/api');
    }

    sv.register = function register(activity){
        return $http.post('/api', activity);

    };

    sv.login = function login(){
        return $http.get('/login');

    };

    sv.logout = function logout(){
        return $http.get('/logout');

    };

    sv.stateGo = function stateGo(state){
        $state.go(state);
    }

});

})()
