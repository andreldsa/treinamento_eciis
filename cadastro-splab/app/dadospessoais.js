(function () {

    var app = angular.module('app');
    app.controller('DadosPessoaisCtrl', function DadosPessoaisCtrl(UserService, SPLabService) {
        vm = this;
        vm.us = UserService;
        Object.defineProperties(vm, {
            user: {
                get: function () { return vm.us.user; },
                set: function (data) { vm.us.user = data; }
            }
        })

        vm.force_num = function (value) {
            if (typeof value != 'string')
                return

            var digits = value.substring(0, Math.min(20, value.length)).split('');
            for (var i=digits.length; i>=0; i--) {
                if (isNaN(digits[i])) {
                    digits.splice(i, 1);
                }
            }
            
            return digits.join('');
        }

        vm.force_cpf = function (value) {
            if (typeof value != 'string')
                return

            var digits = value.substring(0, Math.min(14, value.length)).split('');
            for (var i=digits.length; i>=0; i--) {
                if (isNaN(digits[i])) {
                    digits.splice(i, 1);
                }
            }
            
            if (digits.length > 3) digits.splice(3, 0, '.');
            if (digits.length > 7) digits.splice(7, 0, '.');
            if (digits.length > 11) digits.splice(11, 0, '-');
            vm.user.cpf = digits.join('');
        }

    });
})()
