(function() {

var app = angular.module('app', ['ui.router']);

app.controller('HomeController', function HomeController(DoListService){
    var vm = this;
    vm.tasks = {}

    DoListService.getList().then(
            function sucess(response){
                vm.tasks = response.data;
            }, function error(response){}
        );
    

    vm.activity = {}

    vm.register = function register(){
        DoListService.register(vm.activity).then(
            function sucess(response){
                activity = {};
                return response.data;
        }, function error(response){

        });
    }; 
    
});

app.service('DoListService', function DoListService($http){

    var sv = this;
    sv.getList = function getList(){
      return $http.get('/api');
    }

    sv.register = function register(activity){
        return $http.post('/api', activity);

    };

    sv.loggin = function loggin(){

    }
});



})()
