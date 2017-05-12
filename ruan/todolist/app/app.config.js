(function() {

    angular
        .module('todolistApp')
        .config(['$mdIconProvider', appConfig]);
    
    function appConfig($mdIconProvider) {        
        
        // Angular Material Icons
        $mdIconProvider.fontSet('md', 'material-icons');
    }

})();