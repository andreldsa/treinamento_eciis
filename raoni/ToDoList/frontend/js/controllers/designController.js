/**
 * Created by raoni on 10/05/17.
 */

var design;

(function(){
    angular.module('todoList').controller('designCtrl', function ($mdSidenav, $state){
        design = this;

        design.toggle = function toggle() {
            $mdSidenav('leftNav').toggle();
        };

        design.settings = [
            { name: 'Início', stateTo: 'home', icon: 'home', enabled: true },
            { name: 'Nova Instituição', stateTo: 'institution', icon: 'account_balance', enabled: true },
            { name: 'Novo Usuário', stateTo: 'user.new', icon: 'person_add', enabled: true },
        ];

        design.goTo = function goTo(state) {
            $state.go(state);
            design.toggle();
        };


    });
})();
