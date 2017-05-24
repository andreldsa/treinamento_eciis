(function() {

    angular
        .module('todolistApp')
        .component('header', {
            templateUrl: 'components/header/header.html',
            controller: ['$state', 'UserService', HeaderController],
            controllerAs: 'vm'
        });

    function HeaderController($state, UserService) {
        var vm = this;
        vm.currentNavItem = $state.current.name;

        Object.defineProperties(vm, {
            user: {
                get: function() { return UserService.user; }
            }
        })
    };

})();