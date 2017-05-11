(function() {

    angular
        .module('todolistApp')
        .component('taskCard', {
            templateUrl: 'components/task-card/task-card.html',
            controller: ['TaskService', TaskCardController],
            controllerAs: 'vm',
            bindings: {
                task: '<'
            }
        });
    
    function TaskCardController(TaskService) {
        var vm = this;
        vm.task;
        vm.$onInit = function onInit() {
            initTask();
        };

        function initTask() {
            if(!vm.task){
                console.log("task n existe")
            }
        }
    };

})();