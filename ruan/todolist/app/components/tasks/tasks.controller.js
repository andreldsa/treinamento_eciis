(function() {

    angular
        .module('todolistApp')
        .controller('TasksController', ['TaskService', TasksController]);
        
    function TasksController(TaskService) {
        var vm = this;
        vm.tasks = TaskService.getTasks();
    };
})();
