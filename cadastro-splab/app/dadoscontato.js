(function () {
    var app = angular.module('app');
    app.controller('DadosContatoCtrl', function DadosContatoCtrl(UserService, SPLabService, $timeout, $mdDialog) {
        var vm = this;
        Object.defineProperties(vm, {
            user: {
                get: function () { return UserService.user; },
                set: function (data) { UserService.user = data; }
            }
        })

        vm.splab_email = function (email) {
            return email.split('@')[1] == 'splab.ufcg.edu.br';
        }

        vm.add_email = function (ev) {
            var read_email = $mdDialog.prompt()
                .title('Novo endereço de email')
                .textContent('Digite seu endereço de email')
                .placeholder('email@seila.com')
                .ariaLabel('email')
                .targetEvent(ev)
                .ok('Adicionar')
                .cancel('Cancelar');
            
            $mdDialog.show(read_email)
            .then(function (email) {
                vm.user._state = 'changed';
                vm.user.add_email(email);
            })
        }

        vm.add_fone = function (ev) {
            var read_fone = $mdDialog.prompt()
                .title('Novo telefone')
                .textContent('Digite seu número de telefone')
                .ariaLabel('email')
                .targetEvent(ev)
                .ok('Adicionar')
                .cancel('Cancelar');
            
            $mdDialog.show(read_fone)
            .then(function (fone) {
                vm.user._state = 'changed';
                vm.user.add_fone(fone);
            })
        }

    });
})()
