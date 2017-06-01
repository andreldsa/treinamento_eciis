(function() {

    angular
        .module('todolistApp')
        .controller('AboutController', function AboutController() {
            var vm = this;
            vm.text = "about working";
        });
})();
