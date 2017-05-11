var vm;

function mult(x) {
    var z = 0;
    return function prod(y) {
        z = z + 1;
        return x*y + z;
    };
}


(function () {
    var app = angular.module('BlankApp', ['ngMaterial', 'ui.router']);

    app.config(function ($stateProvider, $urlRouterProvider) {
        $urlRouterProvider.otherwise('/');

        $stateProvider.state('teste', {
            url: '/teste',
            views: {
                'contents': {
                    templateUrl: 'teste.html',
                    controller:'TesteCtrl as vm'
                },
                'footer': {
                    templateUrl: 'about.html',
                    controller:'AboutCtrl as vm'
                }
            }
        })
        .state('about', {
            url: '/about',
            views: {
                'contents': {
                    templateUrl: 'teste.html',
                    controller:'TesteCtrl as vm'
                },
                'footer': {
                    templateUrl: 'about.html',
                    controller:'AboutCtrl as vm'
                }
            }
        });

       $mdThemingProvider.theme('default')
            .primaryPalette('indigo')
            .accentPalette('green')
            .warnPalette('red')
            .backgroundPalette('grey');

        $mdThemingProvider.theme('docs-dark', 'default')
            .primaryPalette('green').dark();

    });

    app.controller('TesteCtrl', function TesteCtrl() {
    });

    app.controller('AboutCtrl', function TesteCtrl($timeout, $state) {

        $timeout(function () {
            $state.go('teste');
        }, 3000);

    });

    app.controller('ExampleController', function ExampleController() {
      var ec = this;
      vm = this;

      ec.del_participante = function del_participante(index) {
        ec.participantes.splice(index, 1);
      }

      ec.participantes = [
        "dalton",
        "andre",
        "jorge",
        "maiana",
        "mayza",
        "tiago",
        "luiz",
        "raoni",
        "ruan",
        "pedro",
        "rafael"
      ];
    });
})()
