(function() {

    angular
        .module('todolistApp')
        .component('listDetails', {
            templateUrl: 'components/list-details/list-details.html',
            controller: ['ListDetailsService', '$stateParams', ListDetailsController],
            controllerAs: 'vm'
        });

    function ListDetailsController(ListDetailsService, $stateParams) {
        var vm = this;
        vm.listId = $stateParams.id;

        vm.$onInit = function onInit(){
            console.log(vm.listId);
        };
    };

})();