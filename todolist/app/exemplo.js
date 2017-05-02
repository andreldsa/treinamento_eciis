var app = angular.module('BlankApp', ['ngMaterial']);
app.controller('ExampleController', function ExampleController() {
  var ec = this;

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
