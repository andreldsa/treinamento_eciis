(function() {
	var app = angular.module('app');
	
	app.controller('TasksCtrl', function TasksCtrl(UserService, $mdDialog) {
		var vm = this;
		vm.save = UserService.save;
    vm.task = {
      name: '',
      description: '',
      deadline: '',
    };

    Object.defineProperties(vm, {
        user: {
            get: function () { return UserService.user; },
            set: function (data) { UserService.user = data; }
        }
    });

   	vm.del_task = function del_task(task, ev) {
   	  var confirm = $mdDialog.confirm()
          .clickOutsideToClose(true)
   	      .title('Deseja finalizar tarefa?')
   	      .textContent('A tarefa ' + '"' + task.name + '"' + ' será finalizada')
   	      .ariaLabel('Lucky day')
   	      .targetEvent(ev)
   	      .ok('Sim')
   	      .cancel('Cancelar');

   	  $mdDialog.show(confirm).then(function() {
        vm.save('del', task);
        vm.showAlert(ev, 'Tarefa finalizada com sucesso');
   	  });
   	};

    vm.add_task = function(ev) {
      vm.save('add', vm.task);
      vm.showAlert(ev,'A tarefa ' + '"' + vm.task.name + '"' + ' foi salva com sucesso');
      vm.clear();
    };

    vm.clear = function clear() {
      vm.task = {
        name: '',
        description: '',
        deadline: ''
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