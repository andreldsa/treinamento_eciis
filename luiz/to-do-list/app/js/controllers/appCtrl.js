(function() {
    var app = angular.module('tarefasApp');

    app.controller('appCtrl', function(taskService) {
        var vm = this;
        Object.defineProperties(vm, {
            user: {
                get: function() {return taskService.user;},
                set: function(data) {taskService.user = data}
            },
        });
    });
})();