(function() {
    var app = angular.module("tarefasApp");
    app.directive("uiTasksView", function() {
        return {
            templateUrl: "partial/tasks-view.html",
            restrict: "E",
            scope: {
                ctrl: "=",
                tasks: "="
            }
        };
    });
})();