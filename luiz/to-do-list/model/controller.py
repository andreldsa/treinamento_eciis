from models import *

class OperacoesTarefas(object):
    
    def criarTarefa(self, nome_tarefa):

        tarefa = Tarefa()
        tarefa.nome_tarefa = nome_tarefa
        tarefa.put()

        return tarefa.key.integer_id()

    def pegarTarefas(self):
        
        query = Tarefa.query()
        tarefas = [todo.to_dict() for todo in query]

        return tarefas