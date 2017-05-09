( function() {

    angular
        .module('todolistApp')
        .component('taskDetails', {
            templateUrl: 'components/task-details/task-details.html',
            controller: TaskDetailsController,
            controllerAs: 'vm'
        });

    function TaskDetailsController() {

    }
})();