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
        vm.userData;
        vm.currentNavItem = $state.current.name; // TODO


        vm.$onInit = function onInit(){
            getUserData();
        };


        function getUserData() {
            UserService.getUserData()
                .then(function(response){
                    vm.userData = response.data;
                }, function error(response) {
                    console.log(response);
                })
        };
    };

})();