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

        Object.defineProperties(vm, {
            lists: {
                get: function() { return ListService.lists; }
            }
        })        
    };

})();