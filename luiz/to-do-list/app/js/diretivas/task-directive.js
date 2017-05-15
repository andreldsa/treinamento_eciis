(function() {
    var app = angular.module("tarefasApp");
    app.directive("uiTasksView", function() {
        return {
            templateUrl: "tasks-view.html",
            restrict: "E",
            scope: {
                tasks: "="
            }
        };
    });
})();