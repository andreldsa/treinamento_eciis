(function() {

    angular
        .module('todolistApp')
        .component('listForm', {
            templateUrl: 'components/list-form/list-form.html',
            controller: ['ListService', '$state', '$stateParams', ListFormController],
            controllerAs: 'vm'
        });

    function ListFormController(ListService, $state, $stateParams) {
        var vm = this;
        var currentState = $state.current.name;
        var listId = $stateParams.listId;
        vm.list;


        vm.$onInit = function onInit() {
            setList();
        };


        function setList() {
            if(typeof listId != 'undefined') {
                getList(listId);
            } else {
                getEmptyList();
            }
        };


        function getList(listId) {
            ListService.getList(listId)
                .then(function(resp) {
                    vm.list = resp.data;
                }, function(err) {
                    console.error(err);
                });
        }


        function getEmptyList() {
            var emptyList = {
                "title": "",
                "description": "",
                "tasks": []
            };

            vm.list = emptyList;
        }


        function goBack() {
            $state.go('lists');
        };


        vm.submit = function submit() {
            if(typeof listId != 'undefined') {
                ListService.updateList(listId, vm.list);
            } else {
                ListService.save(vm.list);
            }
            goBack();
        };
    };
})();