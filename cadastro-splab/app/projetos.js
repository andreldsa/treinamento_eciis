(function () {
    var app = angular.module('app');
    app.controller('ProjetosCtrl', function ProjetosCtrl(UserService, SPLabService, $timeout, $mdDialog) {
        var vm = this;
        Object.defineProperties(vm, {
            user: {
                get: function () { return UserService.user; },
                set: function (data) { UserService.user = data; }
            }
        })

        vm.splab = SPLabService;
        Object.defineProperties(vm, {
            projetos: {
                get: function () { return SPLabService.projetos; }
            }
        })

        vm.del_vinculo = function (index) {
            if (vm.user.del_vinculo(index)) {
                vm.user._state = 'changed';
            }
        }

    });
})()
