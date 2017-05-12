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

        vm.loadTasks = function(){
            requestService.fetchTasks().then(function (response) {
                vm.tasks = response.data;
            });
        };

        vm.putTask = function(data){
            requestService.putTask(data).then(function (response) {
                delete vm.tasks_to_put;

            });
        };

        vm.get = function(what, task){
            return what.task;
        }


    });

})();
