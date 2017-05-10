/**
 * Created by raoni on 08/05/17.
 */
var vm;
(function() {
    angular.module('todoList').config(function($mdIconProvider){
        $mdIconProvider.fontSet('md', 'material-icons');
    });
    angular.module('todoList').controller('taskController', function (requestService) {
        vm = this;
        vm.tasks = [];
        vm.tasks_to_put = [{}];
        vm.loadTasks = function(){
            vm.tasks = vm.requestService.fetchTasks();
        };
        vm.putTasks = function(){
            requestService.putTasks(vm.tasks_to_put);
        };

    });

})();
