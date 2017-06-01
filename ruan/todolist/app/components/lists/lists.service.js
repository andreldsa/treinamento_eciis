(function () {

    angular
        .module('todolistApp')
        .service('ListService', ListService);

    function ListService(){
        var lists = [
            {
                "title": "Livros 2016",
                "description": "Melhores livros do ano",
                "tasks": []
            },
            {
                "title": "Supermercado",
                "description": "compras do mês",
                "tasks": []
            },
            {
                "title": "Semana Acadêmica",
                "description": "Cursos ofercidos",
                "tasks": []
            }
        ];

        this.getLists = function getLists() {
            return lists;
        };
    }
})();