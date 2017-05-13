(function() {

    angular
        .module('todolistApp')
        .component('header', {
            templateUrl: 'components/header/header.html',
            controller: ['$state', HeaderController],
            controllerAs: 'vm'
        });

    function HeaderController($state) {
        var vm = this;

        vm.$onInit = function onInit(){
            vm.state = $state.current;
        };

        vm.$onChange = function() {
            vm.state = $state.current;
        }
    };

})();