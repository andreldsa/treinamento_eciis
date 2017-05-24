(function(){
    var app = angular.module('app');

    app.controller('HomeController', function HomeController(DoListService, $state){
        var vm = this;
        vm.ds = DoListService;

        Object.defineProperties(vm, {
            user: {
                get: function () { return vm.ds.user; },
                set: function (data) { vm.ds.user = data; }
            }
        });

        vm.goTasks = function goTasks(idList, name){
            $state.go('app.task', { 'id': idList , 'name' : name});  
        };

        vm.removeList = function removeList(keyList){
            vm.ds.removeList(keyList).then(
                function sucess(){
                    service.user.removeList(keyList);
                }, function erro(){}
            );
        }        
    });

    app.controller('RgListController', function RgListController(DoListService, $state){    
        var vm = this;
        vm.list = {}

        vm.register = function register(){
            DoListService.rgList(vm.list).then(
                function sucess(response){
                    service.user.addList(response.data);
                    vm.list = {};             
            }, function error(response){
                if(response.status == 401) {
                    $state.go('app.login');
                    }
            });
        };    
    });
})();       