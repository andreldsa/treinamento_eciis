from google.appengine.ext import ndb
import webapp2
import json
from models import *
from util import *

class InstituicaoWebapp(webapp2.RequestHandler):

    def get(self):
    	
		query = Instituicao.query()			
		instituicao = self.request.get('nome')

		if instituicao:		
			query = query.filter(Instituicao.nome_instituicao == instituicao)
		
		dados = [inst.to_dict() for inst in query]
		self.response.headers['Content-Type'] = 'application/json; charset=utf-8'
		self.response.write(data2json(dados))


	def post(self):#Devolve o próprio objeto
		
		dados = json.loads(self.request.body)
		
		cnpj = dados['cnpj']
		
		instituicao = Instituicao(id=cnpj)
		instituicao.nome_instituicao = dados['nome_instituicao']
		instituicao.nome_respons = dados['nome_respons']
		instituicao.cnpj = cnpj
		instituicao.natureza_juridica = dados['natureza_juridica']
		instituicao.endereco = dados['endereco']
		instituicao.area_atuacao = dados['area_atuacao']
		instituicao.descricao = dados['descricao']
		instituicao.imagem = dados.get('imagem')
		instituicao.email = dados['email']
		instituicao.telefone = dados['telefone']
		
		instituicao.put()
		
		self.response.write('{"id": "%s"}' % cnpj)
		self.response.set_status(201)
        

class UsuarioWebapp(webapp2.RequestHandler):
	
	def get(self):
		
		query = Usuario.query()
		
		nome_usuario = self.request.get('nome')
		
		if nome_usuario:		
			query = query.filter(Usuario.nome == nome_usuario)

		dados = [usuario.to_dict() for usuario in query]
		self.response.headers['Content-Type'] = 'application/json; charset=utf-8'
		self.response.write(data2json(dados))
		
	
	def post(self):		#DEVE RETORNAR O OBEJTO, COM O ID NO HEADER
		
		dados = json.loads(self.request.body)
		
		cpf = dados['cpf']
		
		usuario = Usuario(id=cpf)
		usuario.nome= dados['nome']
		usuario.senha = dados['senha']
		usuario.cpf = cpf
		usuario.email = dados['email']
		usuario.foto = dados.get('foto')
		
		usuario.put()
		
		self.response.write('{"id": "%s"}' % cpf)
		self.response.set_status(201)
        

class PostsWebapp(webapp2.RequestHandler):
	
	def get(self):
		
		query = Posts.query()

		
		dados = [post.to_dict() for post in query]
		
		self.response.headers['Content-Type'] = 'application/json; charset=utf-8'
		self.response.write(data2json(dados))
		
	
	def post(self):		
		
		dados = json.loads(self.request.body)
				
		post = Posts()
		post.nome_instituicao = dados['nome_instituicao']
		post.nome_autor = dados['nome_autor']
		post.curtidas = dados['curtidas']
		
		post.put()
		
		self.response.write('{"id": "%s"}' % post.key.integer_id())
		self.response.set_status(201)
        

app = webapp2.WSGIApplication([
    ('/api/instituicao', InstituicaoWebapp),
    ('/api/usuario', UsuarioWebapp),
    ('/api/posts', PostsWebapp),
    
], debug=True)

