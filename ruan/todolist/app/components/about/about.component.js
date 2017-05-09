(function() {

    angular
        .module('todolistApp')
        .component('about', {
            templateUrl: 'components/about/about.html',
            controller: [AboutController],
            controllerAs: 'vm'
        });

    function AboutController() {
        var vm = this;
        vm.text = '';

        vm.$onInit = function onInit(){
            vm.text = "about working";
        };
    };

})();