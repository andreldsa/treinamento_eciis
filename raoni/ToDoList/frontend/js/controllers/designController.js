(function(){
    angular.module('todoList').controller('designCtrl', function ($state, requestService){
        var ctrl = this;
        ctrl.pages = [{name: 'Visualizar Tarefas', state: 'view_tasks'},
                      {name: 'Postar Tarefas', state: 'post_tasks'},
                      {name: 'Início', state: 'home'},
                     ];

        ctrl.goTo = function goTo(state) {
            $state.go(state);
        };
    });
})();
