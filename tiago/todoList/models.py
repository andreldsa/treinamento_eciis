from google.appengine.ext import ndb

class Usuario(ndb.Model):
	keys_tarefas = ndb.IntegerProperty(repeated=True)

	def update(self, data):
		if data.get('operation') == 'add':
			tarefa = Tarefa()
			tarefa.nome = data.get('tarefas')[-1]['nome']
			tarefa.descricao = data.get('tarefas')[-1]['descricao']
			tarefa.prazo = data.get('tarefas')[-1]['prazo']
			key = tarefa.put()
			self.keys_tarefas.append(key.id())

		else:
			tarefaID = data.get('operation')
			self.keys_tarefas.remove(tarefaID)
			ndb.Key(Tarefa, tarefaID).delete()

		self.put()
		tarefas_update = {
			"tarefas": self.get_tarefas()
		}
		return tarefas_update

	def get_tarefas(self):
		tarefas = []

		if len(self.keys_tarefas) > 0:
			for tarefaID in self.keys_tarefas:
				tarefa = Tarefa.get_by_id(tarefaID)
				tarefas.append({
					'nome': tarefa.nome, 
					'descricao': tarefa.descricao, 
					'prazo': tarefa.prazo,
					'id' : tarefaID
				})

		return tarefas

	def get_data(self):
		data = {
			"email": self.key.id(),
			"usuario": self.to_dict(),
			"tarefas": self.get_tarefas()
		}

		return data

class Tarefa(ndb.Model):
	nome = ndb.StringProperty()
	descricao = ndb.StringProperty()
	prazo = ndb.StringProperty()	