import webapp2
from model import User
from model import Task
import json
from utils import *
from google.appengine.api import users
import datetime

def login_required(method):
    def check_login(self, *args):
        user_google = users.get_current_user()
        if user_google is None:
            self.response.set_status(401)
            self.response.headers['Content-Type'] = 'application/json; charset=utf-8'
            self.response.write('{"msg": "erro de autenticacao"}')
            return
        method(self, user_google, *args)
    return check_login

class LoginHandler(webapp2.RequestHandler):

    def get(self):
        self.redirect(users.create_login_url('/'))


class LogoutHandler(webapp2.RequestHandler):

    def get(self):
        user = users.get_current_user()
        if user:
            self.redirect(users.create_logout_url('/'))


class Handler(webapp2.RequestHandler):

    @login_required
    def get(self, user_google):
        user_tasks = User.loadTask(user_google)
        self.response.headers['Content-Type'] = 'application/json; charset=utf-8'
        self.response.write(data2json(user_tasks).encode('utf-8'))

    @login_required
    def post(self, user_google):
        data = json.loads(self.request.body)
        User.createTask(user_google, data)
        self.response.headers['Content-Type'] = 'application/json'
        self.response.set_status(201)


class DeleteHandler(webapp2.RequestHandler):

    @login_required
    def delete(self, user_google, id):
        if User.deleteTask(user_google, id):
            self.response.headers['Content-Type'] = 'application/json'
            self.response.set_status(201)
        else:
            self.response.headers['Content-Type'] = 'application/json'
            self.response.set_status(204)

app = webapp2.WSGIApplication([
    ('/api/tasks', Handler),
    ('/api/delete/(\d+)', DeleteHandler),
    ('/api/login', LoginHandler),
    ('/api/logout', LogoutHandler)

], debug=True)