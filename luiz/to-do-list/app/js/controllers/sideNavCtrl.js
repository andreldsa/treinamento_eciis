(function() {
    var app = angular.module('tarefasApp');
      
    app.controller('sideNavCtrl', function ($timeout, $mdSidenav, $state, taskService) {
        var vm = this;
        vm.toggleLeft = buildToggler('left');
        vm.toggleRight = buildToggler('right');

        vm.changeView = function(view) {
            $state.go(view);
        };

        function buildToggler(componentId) {
            return function() {
                $mdSidenav(componentId).toggle();
            };
        };
    });
})();