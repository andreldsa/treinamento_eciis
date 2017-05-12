/**
 * Created by raoni on 08/05/17.
 */
var vm;
(function() {
    angular.module('todoList').config(function($mdIconProvider){
        $mdIconProvider.fontSet('md', 'material-icons');
    });
    angular.module('todoList').controller('taskController', function (requestService) {
        vm = this;
        vm.tasks = [];

        vm.loadTasks = function(){
            requestService.fetchTasks().then(function (response) {
                vm.tasks = response.data;
            }, function(err){

                if( err.status == 401 ){
                   requestService.login();

                };
            });
        };

        vm.putTask = function(data){
            requestService.putTask(data).then(function (response) {
                console.log(response)
                vm.tasks_to_put = {};
            }, function(err){
                console.log('passou aki');
                console.log(err);
            });
        };



    });

})();
