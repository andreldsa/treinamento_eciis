(function() {

    angular
        .module('todolistApp')
        .component('taskForm', {
            templateUrl: 'components/task-form/task-form.html',
            controller: ['TaskService', TaskFormController],
            controllerAs: 'vm'
        });

    function TaskFormController(TaskService) {
        var vm = this;
        vm.priorities = ['high','medium','low'];
        vm.task = {
            "title": "",
            "description": "",
            "priority": "low"  
        };

        vm.submit = function submit() {
            console.log(vm.task);
            TaskService.save(vm.task)
        };
        
    };
    
})();