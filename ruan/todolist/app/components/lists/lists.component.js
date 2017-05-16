(function() {

    angular
        .module('todolistApp')
        .component('lists', {
            templateUrl: 'components/lists/lists.html',
            controller: ['ListService', ListsController],
            controllerAs: 'vm'
        });

    function ListsController(ListService) {
        var vm = this;
        vm.lists;

        vm.$onInit = function onInit(){
            getLists();
        };

        function getLists() {
          ListService.getLists()
            .then(function(response) {
                vm.lists = response.data;
            })
        }
    };

})();