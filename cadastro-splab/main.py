import webapp2
import json
import datetime
import logging

from google.appengine.api import users
from google.appengine.api import memcache

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


class LogoutHandler(BaseHandler):
    def get(self):
        self.redirect(users.create_logout_url('/'))


class LoginHandler(BaseHandler):

    def get(self):
        uri = self.request.get('uri', '/')
        self.redirect(users.create_login_url(uri))


def login_required(method):
    def check_login(self, *args):
        user = users.get_current_user()
        if user is None:
            self.response.write('{"msg":"requires authentication", "login_url":"http://%s/login"}' % self.request.host)
            self.response.set_status(401)
            return

        method(self, user, *args)

    return check_login


class MainHandler(BaseHandler):

    @login_required
    def get(self, user):
        email = user.email().lower()
        if email.endswith("@splab.ufcg.edu.br") or email.endswith("@ccc.ufcg.edu.br"):
            perfil = Perfil.get_or_insert(email)
            if not perfil.emails:
                perfil.emails.append(email)
                perfil.put()

        else:
            perfil = Perfil.get_by_email(user.email())
            if perfil is None:
                data = {
                    "msg": "email nao cadastrado (%s): faca novo login com email @splab" % user.email(),
                    "login_url": "http://%s/login" % self.request.host,
                    "email": user.email()
                } 
                self.response.write(data2json(data).encode('utf-8'));
                return
            
        user_data = {
            "email": user.email(),
            "perfil": perfil.to_dict(),
            "logout_url": "http://%s/logout" % self.request.host
        }
        self.response.headers['Content-Type'] = 'application/json; charset=utf-8'
        self.response.write(data2json(user_data).encode('utf-8'))


class PerfilHandler(BaseHandler):

    def put(self, perfil_id):
        email = perfil_id
        perfil = Perfil.get_by_email(perfil_id)
        _assert(perfil, 400, "perfil not found")
        data = json.loads(self.request.body)
        perfil.update(data)
        perfil.put()


class ProjetosHandler(BaseHandler):
    def get(self):
        projetos = Projeto.get_all(add=['url', 'key'], remove=[])
        self.response.headers['Content-Type'] = 'application/json; charset=utf-8'
        self.response.write(data2json(projetos).encode('utf-8'))


class PerfilCollectionHandler(BaseHandler):
    def get(self):
            query = Perfil.query()
            perfis = [perfil.to_dict() for perfil in query]
            data = {
                'perfis': perfis,
            }
            self.response.headers['Content-Type'] = 'application/json; charset=utf-8'
            self.response.write(data2json(data))
                

    def post(self):
        data = json.loads(self.request.body)

        # check for existing user with same email
        query = Perfil.query(Perfil.emails == data['email'])
        _assert(query.count() == 0, 400, "email already used by a user")

        # mandatory fields
        perfil = Perfil()
        perfil.nome = data['nome']
        perfil.data_nascimento = datetime.datetime.strptime(data['data_nascimento'], "%Y-%m-%d")
        perfil.lattes = data['lattes']
        perfil.emails = [data['email']]

        # optional fields
        perfil.fones = data.get('fones', [])
        perfil.endereco = data.get('endereco', '')
        perfil.vinculo_ufcg = data.get('vinculo_ufcg')
        perfil.vinculos = data.get('vinculo', [])

        # calculated fields and save
        perfil.checked_at = datetime.datetime.now()
        perfil.put()

        # response
        self.response.write('{"iid": "%d"}' % perfil.key.integer_id())
        self.response.set_status(201)


app = webapp2.WSGIApplication([
    ('/login', LoginHandler),
    ('/logout', LogoutHandler),
    ('/api', MainHandler),
    ('/api/perfil', PerfilCollectionHandler),
    ('/api/perfil/(.*)', PerfilHandler),
    ('/api/projetos', ProjetosHandler),
], debug=True)

def erro404(request, response, exception):
    response.set_status(exception.code)
    response.write("url invalida: " + str(exception))

app.error_handlers[404] = erro404
