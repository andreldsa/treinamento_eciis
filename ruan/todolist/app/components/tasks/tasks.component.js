(function() {

    angular
        .module('todolistApp')
        .component('tasks', {
            templateUrl: 'components/tasks/tasks.html',
            controller: ['TaskService', TasksController],
            controllerAs: 'vm'
        });
    
    function TasksController(TaskService) {
        var vm = this;
        vm.tasks = [];

        vm.$onInit = function onInit() {
            vm.tasks = TaskService.getAll();
        };
    };

})();