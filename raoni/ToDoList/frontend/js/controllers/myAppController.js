(function(){
    angular.module('todoList').controller('myAppCtrl', function(requestService){
        var myApp = this;
        Object.defineProperties(myApp, {
            user: {
                get: function () { return requestService.user; },
                set: function (boolean) { requestService.user = boolean; }
            }
        });

        myApp.fazTeuNome = function(){
            user = true;
        };
    });
})();