(function() {

    angular
        .module('todolistApp')
        .component('listDetails', {
            templateUrl: 'components/list-details/list-details.html',
            controller: ['ListService', 'TaskService', '$stateParams', ListDetailsController],
            controllerAs: 'vm'
        });

    function ListDetailsController(ListService, TaskService, $stateParams) {
        var vm = this;
        vm.list;
        vm.tasks = [];
        var listId = $stateParams.listId;


        vm.$onInit = function onInit(){
            getList();
            getTasks();
        };


        var getList = function getList(){
            ListService.getList(listId)
                .then(function(response) {
                    vm.list = new List(response.data);
                })          
        }


        vm.noTasks = function noTask(){
            return vm.tasks.length == 0;
        }


        var getTasks = function getTasks() {
            TaskService.getTasksFromList(listId)
                .then(function(response) {
                    vm.tasks = response.data;
                });
        };



        vm.changeDone = function changeDone(task) {
            task.done = !task.done;
            TaskService.updateTask(listId, task.id, task);
        };


        vm.editTask = function editTask(task) {
            console.log('edit');
        };


        vm.deleteTask = function deleteTask(taskId) {
            TaskService.deleteTask(vm.list.id, taskId)
                .then(function(response) {
                    _.remove(vm.tasks, function(task) {
                        return task.id == response.data.id;
                    });
                }, function(err) {
                    console.error(err);
                });
        };
    };
})();