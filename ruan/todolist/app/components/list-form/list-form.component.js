(function() {

    angular
        .module('todolistApp')
        .component('listForm', {
            templateUrl: 'components/list-form/list-form.html',
            controller: ['ListService', ListFormController],
            controllerAs: 'vm'
        });

    function ListFormController(ListService) {
        var vm = this;

        vm.$onInit = function onInit() {
            resetForm();
        };


        function resetForm() {
            vm.list = {
                "title": "",
                "description": "",
                "tasks": []
            };
        };


        vm.submit = function submit() {
            ListService.save(vm.list);
            resetForm();
        };
    };
})();