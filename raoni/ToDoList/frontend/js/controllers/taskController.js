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
            }, function(err){
                if( err.status == 401 ){
                   requestService.login();
                };
            });
        };

        vm.putTask = function(data){
            requestService.putTask(data).then(function (response) {
                vm.tasks_to_put = {};
            }, function(err){
                if( err.status == 401 ){
                    requestService.login();
                };
            });
        };

        vm.deleteTasks = function(name){
            requestService.deleteTasks(name).then(function(response) {
                vm.tasks_to_delete = {};
                if(response.status === 204){
                    alert('Essa tarefa não existe')
                }
            }, function (err) {
                if( err.status == 401 ){
                    requestService.login();
                };
            });
        };
    });
})();
