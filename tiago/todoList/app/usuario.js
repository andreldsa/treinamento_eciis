"use strict";
function Usuario(data) {
    data = data || {}
    _.extend(this, data)
};

Usuario.prototype.del_tarefa = function(tarefaID) {
	_.remove(this.tarefas, tarefa => tarefa.id === tarefaID);
};

Usuario.prototype.add_tarefa = function(tarefa) {
    this.tarefas.push(tarefa);
};