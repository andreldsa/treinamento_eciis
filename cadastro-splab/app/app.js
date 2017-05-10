"use strict";
var vm;
(function (){
    moment.locale('pt-br');
    var app = angular.module('app', ['ngMaterial', 'ui.router']);

    app.config(function config($mdIconProvider, $mdDateLocaleProvider, $stateProvider, $urlRouterProvider, $mdThemingProvider) {
        // configurações de states
        $urlRouterProvider.otherwise('/');
        $stateProvider
        .state('app', {
            'abstract': true,
            'views': {
                'header': {
                    templateUrl: 'partial/header.html'
                }
            }
        })
        .state('app.home', {
            'url': '/',
            'views': {
                'contents@': {
                    templateUrl: 'partial/home.html'
                },
            }
        })
        .state('app.dpessoais', {
            'url': '/dp',
            'views': {
                'contents@': {
                    templateUrl: 'partial/dados_pessoais.html',
                    controller: 'DadosPessoaisCtrl as vm'
                },
            }
        })
        .state('app.dcontato', {
            'url': '/dc',
            'views': {
                'contents@': {
                    templateUrl: 'partial/dados_contato.html',
                    controller: 'DadosContatoCtrl as vm'
                },
            }
        })
        .state('app.projetos', {
            'url': '/p',
            'views': {
                'contents@': {
                    templateUrl: 'partial/projetos.html',
                    controller: 'ProjetosCtrl as vm'
                },
            }
        })
        .state('app.testes', {
            'url': '/t',
            'views': {
                'contents@': {
                    templateUrl: 'partial/testes.html',
                    controller: 'TestesCtrl as vm'
                },
            }
        })
        

        // temas
        $mdThemingProvider.theme('default')
            .primaryPalette('indigo')
            .accentPalette('green')
            .warnPalette('red')
            .backgroundPalette('grey');

        $mdThemingProvider.theme('docs-dark', 'default')
            .primaryPalette('green').dark();


        // configurações de ícones
        $mdIconProvider.fontSet('md', 'material-icons');

        // configurações de datas e horas
        $mdDateLocaleProvider.months = ['janeiro', 'fevereiro', 'março', 'abril', 'maio', 'junho', 'julho', 'agosto', 'setembro', 'outubro', 'novembro', 'dezembro'];
        $mdDateLocaleProvider.shortMonths = ['Jan', 'Fev', 'Mar', 'Abr', 'Mai', 'Jun', 'Jul', 'Ago', 'Set', 'Out', 'Nov', 'Dez'];
        $mdDateLocaleProvider.days = ['domingo', 'segunda-feira', 'terça-feira', 'quarta-feira', 'quinta-feira', 'sexta-feira',  'sábado'];
        $mdDateLocaleProvider.shortDays = ['Dom', 'Seg', 'Ter', 'Qua', 'Qui', 'Sex',  'Sáb'];
        $mdDateLocaleProvider.parseDate = function(dateString) {
            var m = moment(dateString, 'D/M/YYYY', true);
            return m.isValid() ? m.toDate() : new Date(NaN);
        };
        $mdDateLocaleProvider.formatDate = function(date) {
              var m = moment(date);
              //return m.isValid() ? m.format('L') : '';
              return m.isValid() ? m.format('L') : '';
        };

    });

    app.controller('AppCtrl', function AppCtrl(UserService) {
        vm = this;
        vm.save_user = UserService.save;
        Object.defineProperties(vm, {
            user: {
                get: function () { return UserService.user; },
                set: function (data) { UserService.user = data; }
            },
            eh_perfil: {
                get: function () { return vm.user instanceof Perfil; }
            }
        })

    });

    app.controller('TestesCtrl', function TestesCtrl(UserService) {
        var vm = this;
        vm.us = UserService;
        Object.defineProperties(vm, {
            user: {
                get: function () { return UserService.user; },
                set: function (data) { UserService.user = data; }
            }
        })

        vm.testando = [1,2,3,4];
    });

})()
