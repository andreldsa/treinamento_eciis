var vm;

(function() {
  var app = angular.module('todoListApp', ['ngMaterial']);
  app.config(function($mdIconProvider) {
    $mdIconProvider.fontSet('md', 'material-icons');
  }); 
  app.controller('ToDoController', function ToDoController() {
    vm = this;
    vm.tarefas = [];
    vm.tarefa = {};
    vm.items = [
      {name: 'Sign Out', link: '/api/logout'},
      {name: 'About'}
    ];

    vm.del_tarefa = function del_tarefa(index) {
      vm.tarefas.splice(index, 1);
    };

    vm.save = function save() {
      vm.tarefas.push(vm.tarefa);
      vm.clear();
    };

    vm.clear = function clear() {
      vm.tarefa = {};
    };
  });
})();