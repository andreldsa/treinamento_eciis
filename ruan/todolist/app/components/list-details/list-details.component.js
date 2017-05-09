(function() {

    angular
        .module('todolistApp')
        .component('listDetails', {
            templateUrl: 'components/list-details/list-details.html',
            controller: ['ListDetailsService', ListDetailsController],
            controllerAs: 'vm'
        });

    function ListDetailsController(ListDetailsService) {
        var vm = this;
        vm.text = '';

        vm.$onInit = function onInit(){
            vm.text = "list details working";
        };
    };

})();