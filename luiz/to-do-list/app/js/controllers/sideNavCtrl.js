(function() {
    var app = angular.module('tarefasApp');
      
    app.controller('sideNavCtrl', function ($timeout, $mdSidenav, $state, todoService) {
        var vm = this;
        vm.toggleLeft = buildToggler('left');
        vm.toggleRight = buildToggler('right');

        vm.changeView = function(view) {
            $state.go(view);
        };

        vm.login = function() {
            todoService.login();
        };

        vm.logout = function() {
            todoService.logout();
        };

        function buildToggler(componentId) {
            return function() {
                $mdSidenav(componentId).toggle();
            };
        };
    });
})();