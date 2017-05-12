(function() {

    angular
        .module('todolistApp')
        .component('listDetails', {
            templateUrl: 'components/list-details/list-details.html',
            controller: ['ListService', '$stateParams', ListDetailsController],
            controllerAs: 'vm'
        });

    function ListDetailsController(ListService, $stateParams) {
        var vm = this;
        vm.list;

        vm.$onInit = function onInit(){
            getList();
        };

        var getList = function getList(){
            ListService.getOne($stateParams.id)
                .then(function(response) {
                    vm.list = response.data;
                })          
        }

    };

})();