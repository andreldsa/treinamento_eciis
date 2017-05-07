(function() {

    angular
        .module('todolistApp')
        .controller('TasksController', function TasksController() {
            var vm = this;
            vm.text = "tasks working";
        });
})();
