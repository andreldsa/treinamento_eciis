(function(){
    var app = angular.module('app');

    app.controller('HomeController', function HomeController(DoListService, $state){
    var vm = this;
    vm.lists = {}

    DoListService.getList().then(
            function sucess(response){
                vm.lists = response.data;
            }, function error(response){
                if(response.status == 401) {
                    $state.go('app.login');
                }
            }
    );

     vm.goTasks = function goTasks(idList){
         $state.go('app.task', { 'id': idList });  
    };        
});

app.controller('RgListController', function RgListController(DoListService, $state){    
    var vm = this;
    vm.list = {}

    vm.register = function register(){
        DoListService.rgList(vm.list).then(
            function sucess(response){
                DoListService.user.lists.push(response.data.name)
                vm.list = {};
                
        }, function error(response){
             if(response.status == 401) {
                   $state.go('app.login');
                }
        });
    };    
});
})();