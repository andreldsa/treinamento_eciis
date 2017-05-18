var vm;
(function() {
    angular.module('todoList').config(function($mdIconProvider){
        $mdIconProvider.fontSet('md', 'material-icons');
    });

    angular.module('todoList').controller('taskController', function (requestService) {
        vm = this;
        vm.tasks = [];
        vm.task_name = '';
        vm.task_description = '';
        vm.task_deadline = '';


        vm.createTask = function(name, description, deadline){
          task = new Task({name: name, description: description, deadline: deadline});
          vm.task_name = '';
          vm.task_description = '';
          vm.task_deadline = '';
          vm.putTask(task);
        };

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
            }, function(err){
                if( err.status == 401 ){
                    requestService.login();
                };
            });
        };

        vm.synchronizeTask = function(id){
            for(var i=vm.tasks.length-1; i>=0; i--){
                if(vm.tasks[i].id == id){
                    vm.tasks.splice(i, 1);
                };
            };
        };

        vm.deleteTasks = function(id){
            requestService.deleteTasks(id).then(function(response) {
                if(response.status === 204){
                    alert('Essa tarefa não existe');
                }
                else{
                    vm.synchronizeTask(id);
                }
            }, function (err) {
                if( err.status == 401 ){
                    requestService.login();
                };
            });
        };
    });
})();
