(function() {

    angular
        .module('todolistApp')
        .component('home', {
            templateUrl: 'components/home/home.html',
            controller: ['$state', 'UserService', HomeController],
            controllerAs: 'vm'
        });

    function HomeController($state, UserService) {
        var vm = this;

        Object.defineProperties(vm, {
            user: {
                get: function() { return UserService.user; }
            }
        });


        
    };

})();