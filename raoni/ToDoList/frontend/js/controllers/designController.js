/**
 * Created by raoni on 10/05/17.
 */
(function(){
    angular.module('todoList').controller('designCtrl', function ($state){
        var ctrl = this;

        ctrl.pages = [{name: 'Visualizar Tarefas', state: 'view_tasks'},
                      {name: 'Postar', state: 'post_tasks'},
                      {name: 'Início', state: 'home'}];

        ctrl.goTo = function goTo(state) {
            $state.go(state);

        };




    });
})();
