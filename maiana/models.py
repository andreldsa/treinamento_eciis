from google.appengine.ext import ndb

class Instituicao(ndb.Model):
	nome_instituicao = ndb.StringProperty(required=True)
	nome_respons = ndb.StringProperty(required=True)
	cnpj = ndb.StringProperty(required=True) #repeated=False por default
	natureza_juridica = ndb.StringProperty(required=True,
			choices = set(["publico", "privado", "filantropico"])) # Pode fazer isso ?
	endereco = ndb.TextProperty(required=True)
	area_atuacao = ndb.StringProperty(required=True)
	descricao = ndb.TextProperty(required=True)
	imagem = ndb.GenericProperty()
	email = ndb.StringProperty(required=True)
	telefone = ndb.StringProperty(required=True)

class Usuario(ndb.Model):
	nome = ndb.StringProperty(required=True) # e o nome ou o login ?
	senha = ndb.StringProperty(required=True)
	cpf = ndb.StringProperty(required=True)
	email = ndb.StringProperty(required=True)
	foto = ndb.GenericProperty()


class Posts(ndb.Model):
	nome_instituicao = ndb.StringProperty(required=True)
	nome_autor = ndb.StringProperty(required=True)
	data_publicacao = ndb.DateTimeProperty(auto_now_add=True)
	curtidas = ndb.IntegerProperty(required=True)

