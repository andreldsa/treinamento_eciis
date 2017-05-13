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
        vm.list = [];
        vm.tasks = [];
        var listId = $stateParams.listId;


        vm.$onInit = function onInit(){
            getList();
            getTask();
        };


        var getList = function getList(){
            ListService.getOne(listId)
                .then(function(response) {
                    vm.list = response.data;
                })          
        }


        vm.noTasks = function noTask(){
            return vm.tasks.length == 0;
        }


        var getTask = function getTasks() {
            TaskService.getAllFromList(listId)
                    .then(function(response) {
                        vm.tasks = response.data;
                    })
        }

        vm.changeDone = function changeDone(task) {
            task.done = !task.done;
        }


        vm.editTask = function editTask(task) {
            console.log('edit');
        }


        vm.deleteTask = function deleteTask(task) {
            console.log('delte');
        }


    };

})();