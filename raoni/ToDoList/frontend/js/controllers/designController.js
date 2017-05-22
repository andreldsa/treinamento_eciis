(function(){
    angular.module('todoList').controller('designCtrl', function ($state, requestService){
        var ctrl = this;

        ctrl.pages = [{name: 'Visualizar Tarefas', state: 'app.view_tasks'},
                      {name: 'Postar Tarefas', state: 'app.post_tasks'},
                      {name: 'Início', state: 'app.home'}
                     ];

        ctrl.goTo = function goTo(state) {
            $state.go(state);
        };
    });
})();