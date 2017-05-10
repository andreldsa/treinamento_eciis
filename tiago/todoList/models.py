from google.appengine.ext import ndb

class User(ndb.Model):
	pass
	# NOT IMPLEMENTED YET

class Tarefa(ndb.Model):
	name = ndb.StringProperty()
	descricao = ndb.StringProperty()
	data = ndb.StringProperty()	