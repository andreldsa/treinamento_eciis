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
        vm.userData;

        vm.$onInit = function onInit(){
            getUserData();
        };

        function getUserData() {
            UserService.getUserData()
                .then(function(response){
                    vm.userData = response.data;
                }, function error(response) {
                    console.log('Error:' + JSON.stringify(response));
                });
        };
    };

})();