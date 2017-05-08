import webapp2
import sys

sys.path.append("model")
sys.path.append("util")

from models import Tarefa
from controller import *
from util import *

class MainHandler(webapp2.RequestHandler):

    def get(self):

        operacoes = OperacoesTarefas()

        data = operacoes.pegarTarefas()

        self.response.headers['Content-Type'] = 'application/json; charset=utf-8'
        self.response.write(data2json(data))

    def post(self):

        data = json2data(self.request.body)

        operacoes = OperacoesTarefas()

        id = operacoes.criarTarefa(data['nome_tarefa'])

        self.response.set_status("201")
        self.response.write(id)
        self.response.write("\n")



app = webapp2.WSGIApplication([
    ("/api/todo", MainHandler),
], debug=True)
