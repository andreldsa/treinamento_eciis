
import webapp2
import sys
import json

sys.path.append("model")

from controller import *

def date_handler(obj):
  if hasattr(obj, 'isoformat'):
    return obj.isoformat()
  elif hasattr(obj, 'email'):
    return obj.email()

  return obj

def data2json(data):
  return json.dumps(
    data,
    default=date_handler,
    indent=2,
    separators=(',', ': '),
    ensure_ascii=False)

class MainHandler(webapp2.RequestHandler):
    def get(self):
        self.response.write("Deu certo")

class ApInstituicao(webapp2.RequestHandler):
    def get(self):
        tipo_busca = self.request.get("tipo_busca")

        operacao = OpracoesInstituicao()

        if tipo_busca == 'todas':
            resultado_busca = operacao.buscarTodasAsInstituicoes()
        else:
            resultado_busca = operacao.buscarInstituicaoPorNome(tipo_busca)

        resultado_busca = [instituicao.to_dict() for instituicao in resultado_busca]
        self.response.write(data2json(resultado_busca))

    def post(self):

        data = json.loads(self.request.body)

        operacao = OpracoesInstituicao()

        operacao.criarInstituicao(data['nome_instituicao'], data['nome_resposavel'],
            data['cpnj'], data['natureza'], data['endereco'], data['area_atuacao'],
            data['email_contato'], data['telefone_contato'], data['descricao'])

class ApiUser(webapp2.RequestHandler):

    def get(self):

        operacao = OperacoesUser()
        resultado_busca = [user.to_dict() for user in operacao.buscarTodosUsuarios()]

        self.response.write(data2json(resultado_busca))

    def post(self):
        data = json.loads(self.request.body)
        operacao = OperacoesUser()

        operacao.cadastrarUsuario(data['nome'], data['senha'], data['cpf'], data['email'])

class ApiPost(webapp2.RequestHandler):

    def get(self):
        operacao = OperacoesPost()
        resultado_busca = [post.to_dict() for post in operacao.buscarTodosPosts()]

        self.response.write(data2json(resultado_busca))

    def post(self):
        data = json.loads(self.request.body)
        operacao = OperacoesPost()

        operacao.criarPost(data['nome_instituicao'], data['nome_autor'], data['num_curtidas'])

app = webapp2.WSGIApplication([
    ("/api/instituicao", ApInstituicao),
    ("/api/user", ApiUser),
    ("/api/post", ApiPost),
    ("/", MainHandler),
], debug=True)