import webapp2
import json
import datetime
import logging

from google.appengine.api import users

from models import *
from utils import *

def _assert(condition, status_code, msg):
    if condition:
        return

    logging.info("assertion failed: %s" % msg)
    webapp2.abort(status_code, msg)


class BaseHandler(webapp2.RequestHandler):
    def handle_exception(self, exception, debug):
        logging.error(str(exception))
        self.response.write("oops! %s\n" % str(exception))


class InitHandler(BaseHandler):
    def get(self):

        query = Projeto.get_all()
        if query.count():
            self.response.headers['Content-Type'] = 'application/json; charset=utf-8'
            self.response.write('{"msg":"nothing done!!! database ALREADY initialized!", "projetos_url":"http://%s/api/projetos"}' % self.request.host)
            return 


        # epol
        epol = Projeto()
        epol.nome = "ePol 2"
        epol.coordenador = "joao.arthur@computacao.ufcg.edu.br"
        epol.colaboradores = [
            'jorge.figueiredo@computacao.ufcg.edu.br',
            'dalton@computacao.ufcg.edu.br',
            'franklin@computacao.ufcg.edu.br',
            'tiago@computacao.ufcg.edu.br',
        ]
        epol.inicio_at = datetime.datetime.strptime('2016-12-01', '%Y-%m-%d').date()
        epol.put()


        # e-ciis
        bazooka = Projeto()
        bazooka.nome = "Bazooka"
        bazooka.coordenador = "jorge@splab.ufcg.edu.br"
        bazooka.colaboradores = [
            'dalton@splab.ufcg.edu.br',
        ]
        bazooka.inicio_at = datetime.datetime.strptime('2017-04-31', '%Y-%m-%d').date()
        bazooka.put()


        # bazooka
        bazooka = Projeto()
        bazooka.nome = "Bazooka"
        bazooka.coordenador = "wilkerson@computacao.ufcg.edu.br"
        bazooka.colaboradores = [
            'adalberto@computacao.ufcg.edu.br',
        ]
        bazooka.inicio_at = datetime.datetime.strptime('2016-12-01', '%Y-%m-%d').date()
        bazooka.put()


        # epol
        epol = Projeto()
        epol.nome = "ePol 1"
        epol.coordenador = 'dalton@computacao.ufcg.edu.br'
        epol.colaboradores = [
            "joao.arthur@computacao.ufcg.edu.br",
            'jorge.figueiredo@computacao.ufcg.edu.br',
            'franklin@computacao.ufcg.edu.br',
            'tiago@computacao.ufcg.edu.br',
        ]
        epol.inicio_at = datetime.datetime.strptime('2010-05-10', '%Y-%m-%d').date()
        epol.fim_at = datetime.datetime.strptime('2016-11-30', '%Y-%m-%d').date()
        epol.put()

        self.response.headers['Content-Type'] = 'application/json; charset=utf-8'
        self.response.write('{"msg":"database initialized with a few projects", "projetos_url":"http://%s/api/projetos"}' % self.request.host)


app = webapp2.WSGIApplication([
    ('/admin/init', InitHandler),
], debug=True)

def erro404(request, response, exception):
    response.write("url invalida: " + str(exception))

app.error_handlers[404] = erro404
