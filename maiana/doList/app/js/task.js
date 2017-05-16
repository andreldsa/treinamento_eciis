(function(){
    var app = angular.module('app');
app.controller('TaskController', function TaskController(DoListService, $state, $stateParams){
    var vm = this;
    vm.tasks = {};
    vm.list= $stateParams.id;
    
    DoListService.getTask(vm.list).then(
        function sucess(response){
            vm.tasks = response.data;
        }, function error(response){
            if(response.status == 401) {
                $state.go('app.login');
            }
        }
    );      
});

app.controller('RgTaskController', function RgTaskController(DoListService, $state){    
    vm = this;
    vm.ds = DoListService;
    vm.activity = {};
    vm.list = "";

    Object.defineProperties(vm, {
        user: {
            get: function () { return vm.ds.user; },
            set: function (data) { vm.ds.user = data; }
        }
    });

    vm.register = function register(){
        DoListService.rgTask(vm.list, vm.activity).then(
            function sucess(response){
                vm.activity = {};
                vm.list = "";

                return response.data;
        }, function error(response){
             if(response.status == 401) {
                   $state.go('app.login');
                }
        });
    };  
});
})();