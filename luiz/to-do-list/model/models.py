#Luiz Fernando da Silva

from google.appengine.ext import ndb

class Tarefa(ndb.Model):

    nome_tarefa = ndb.StringProperty(required=True)
    date = ndb.DateTimeProperty(auto_now_add=True)

class User(ndb.Model):

    email = ndb.StringProperty(required=True)
    todo_list = ndb.KeyProperty(kind='Tarefa', repeated=True)