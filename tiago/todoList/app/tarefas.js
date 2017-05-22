(function() {
	var app = angular.module('app');
	
	app.controller('TarefasCtrl', function TarefasCtrl(UserService, $mdDialog) {
		var vm = this;
		vm.save = UserService.save;
    vm.delete = UserService.delete;
    vm.tarefa = {
      nome: '',
      descricao: '',
      prazo: '',
    };

    Object.defineProperties(vm, {
        user: {
            get: function () { return UserService.user; },
            set: function (data) { UserService.user = data; }
        }
    });

   	vm.del_tarefa = function del_tarefa(tarefa, ev) {
   	  var confirm = $mdDialog.confirm()
          .clickOutsideToClose(true)
   	      .title('Deseja finalizar tarefa?')
   	      .textContent('A tarefa ' + '"' + tarefa.nome + '"' + ' será finalizada')
   	      .ariaLabel('Lucky day')
   	      .targetEvent(ev)
   	      .ok('Sim')
   	      .cancel('Cancelar');

   	  $mdDialog.show(confirm).then(function() {
        vm.save('del', tarefa);
        vm.showAlert(ev, 'Tarefa finalizada com sucesso');
   	  });
   	};

    vm.add_tarefa = function(ev) {
      vm.save('add', vm.tarefa);
      vm.showAlert(ev,'A tarefa ' + '"' + vm.tarefa.nome + '"' + ' foi salva com sucesso');
      vm.clear();
    };

    vm.clear = function clear() {
      vm.tarefa = {
        nome: '',
        descricao: '',
        prazo: ''
      };
    };

    vm.showAlert = function showAlert(ev, message) {
      $mdDialog.show(
      $mdDialog.alert()
        .parent(angular.element(document.querySelector('#popupContainer')))
        .clickOutsideToClose(true)
        .title('Sucesso')
        .textContent(message)
        .ariaLabel('Alert Dialog Demo')
        .ok('Entendi')
        .targetEvent(ev)
      );
    };
	});
})();