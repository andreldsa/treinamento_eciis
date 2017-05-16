(function() {

    angular
        .module('todolistApp')
        .component('taskForm', {
            templateUrl: 'components/task-form/task-form.html',
            controller: ['TaskService', '$stateParams', '$state', '$timeout', TaskFormController],
            controllerAs: 'vm'
        });

    function TaskFormController(TaskService, $stateParams, $state, $timeout) {
        var vm = this;
        vm.priorities = ['high','medium','low'];
        var listId = $stateParams.listId;

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


        function goBack() {
            $state.go('list-details',{listId: listId});
        }
        
        
        vm.submit = function submit() {
            TaskService.save(listId, vm.task);
            $timeout(goBack(),100);
        };
        
    };
    
})();