
from google.appengine.ext import ndb

class Instituicao(ndb.Model):
    nome_instituicao = ndb.StringProperty(required=True)
    nome_resposavel = ndb.StringProperty(required=True)
    cpnj = ndb.StringProperty(required=True)
    natureza = ndb.StringProperty(required=True, choices=set(["Publico", "Privado", "Filantropico"]))
    endereco = ndb.StringProperty(required=True)
    area_atuacao = ndb.StringProperty(required=True)
    descricao = ndb.TextProperty()
    email_contato = ndb.StringProperty(required=True)
    telefone_contato = ndb.StringProperty(required=True)

class User(ndb.Model):
    nome = ndb.StringProperty(required=True)
    senha = ndb.StringProperty(required=True)
    cpf = ndb.StringProperty(required=True)
    email = ndb.StringProperty(required=True)

class Post(ndb.Model):
    nome_instituicao= ndb.StringProperty(required=True)
    nome_autor = ndb.StringProperty(required=True)
    data_criacao = ndb.DateTimeProperty(auto_now_add=True)
    num_curtidas = ndb.IntegerProperty(default=0)