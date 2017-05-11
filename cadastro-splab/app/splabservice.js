(function () {
    var app = angular.module('app');
    app.service('SPLabService', function SPLabService($http, $q) {
        var service = this;
        var _projetos = null;
        Object.defineProperties(service, {
            projetos: {
                get: function () { return _projetos; }
            }
        })

        $http.get('/api/projetos')
        .then(function (response) {
            // ok
            _projetos = response.data;
        }, function (err) {
            //
            alert('não foi possível ler projetos')
        })
    });
})()
