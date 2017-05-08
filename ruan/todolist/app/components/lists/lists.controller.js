(function() {

    angular
        .module('todolistApp')
        .controller('ListsController', ['ListService', ListsController]);
        
    function ListsController(ListService) {
        var vm = this;
        vm.lists = ListService.getLists();
    };
})();
