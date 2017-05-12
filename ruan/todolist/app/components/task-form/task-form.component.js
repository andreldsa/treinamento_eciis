(function() {

    angular
        .module('todolistApp')
        .component('taskForm', {
            templateUrl: 'components/task-form/task-form.html',
            controller: ['TaskService', '$stateParams', TaskFormController],
            controllerAs: 'vm'
        });

    function TaskFormController(TaskService, $stateParams) {
        var vm = this;
        vm.priorities = ['high','medium','low'];

        vm.$onInit = function onInit() {
            resetForm();
        }

        function resetForm() {
            vm.task = {
                "title": "",
                "description": "",
                "priority": "low"  
            };
        };
        
        vm.submit = function submit() {
            TaskService.save($stateParams.listId, vm.task);
            resetForm();
        };
        
    };
    
})();