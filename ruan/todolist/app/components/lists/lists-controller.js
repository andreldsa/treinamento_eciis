(function() {

    angular
        .module('todolistApp')
        .controller('ListsController', function ListsController() {
            var vm = this;
            vm.text = "lists working";
        });
})();
