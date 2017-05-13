from google.appengine.ext import ndb

class Usuario(ndb.Model):
	tarefas = ndb.KeyProperty(kind='Tarefa', repeated=True)

class Tarefa(ndb.Model):
	nome = ndb.StringProperty()
	descricao = ndb.StringProperty()
	prazo = ndb.StringProperty()	