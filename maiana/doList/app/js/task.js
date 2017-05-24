var vm
(function(){
    var app = angular.module('app');
    app.controller('TaskController', function TaskController(DoListService, $state, $stateParams){
        vm = this;
        vm.tasks = [];
        vm.list= {'id' : $stateParams.id,
                    'name' : $stateParams.name};
        
        DoListService.getTask(vm.list.id).then(
            function sucess(response){
                vm.tasks = response.data;
            }, function error(response){
                if(response.status == 401) {
                    $state.go('app.login');
                }
            }
        );
        vm.removeTask = function removeTask(task){
            DoListService.removeTask(vm.list.id, task).then(
                function sucess(response){
                    _.remove(vm.tasks, function(activity) {
                       return activity.name == task;
                    });
                    return response.data;   
            }, function error(response){
                if(response.status == 401) {
                    $state.go('app.login');
                    }
            });
        };

        vm.concluida = function concluida(task){
            task.status = true;
             DoListService.updateTask(vm.list.id, task.id).then(
                function sucess(response){   
            }, function error(response){});
        }      
    });

    app.controller('RgTaskController', function RgTaskController(DoListService, $state){    
        vm = this;
        vm.ds = DoListService;
        vm.activity = {};
        vm.list = {'id' : "",
                    'name' : ""};

        Object.defineProperties(vm, {
            user: {
                get: function () { return vm.ds.user; },
                set: function (data) { vm.ds.user = data; }
            }
        });

        vm.register = function register(){
            DoListService.rgTask(vm.list.id, vm.activity).then(
                function sucess(response){
                    vm.activity = {};
                    vm.list = {};

                    console.log(response.data)

                    return response.data;
            }, function error(response){});
        };    
    });
})();