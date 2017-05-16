import webapp2

from model import User
from model import Task

import json

from utils import *
from google.appengine.api import users

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
            self.redirect(users.create_logout_url(''))


class Handler(webapp2.RequestHandler):

    @login_required
    def get(self, user_google):
        user_email = user_google.email()
        user = User.get_or_insert(user_email, email=user_email)
        user_tasks = [task.get().to_dict() for task in user.tasks]
        self.response.headers['Content-Type'] = 'application/json; charset=utf-8'
        self.response.write(data2json(user_tasks).encode('utf-8'))

    @login_required
    def post(self, user_google):
        user_email = user_google.email()
        user = User.get_or_insert(user_email, email=user_email)
        data = json.loads(self.request.body)
        task = Task(id = data['name'])
        task.name = data['name']
        task.description = data['description']
        task_key = task.put()
        user.tasks.append(task_key)
        user.put()
        self.response.headers['Content-Type'] = 'application/json'
        self.response.set_status(201)


class DeleteHandler(webapp2.RequestHandler):
    @login_required
    def delete(self, user_google, name):
        user_email = user_google.email()
        user = User.get_by_id(user_email)
        user_tasks = [task.get() for task in user.tasks]
        task_name = name.split('/')[0]
        finded = False
        for i in xrange(len(user_tasks)):
            if user_tasks[i].name == task_name:
                user.tasks[i].delete()
                user.tasks.pop(i)
                user.put()
                finded = True
                self.response.headers['Content-Type'] = 'application/json'
                self.response.set_status(201)
                break

        if not finded:
            self.response.headers['Content-Type'] = 'application/json'
            self.response.set_status(204)

app = webapp2.WSGIApplication([
    ('/api/tasks', Handler),
    ('/api/delete/(.*)', DeleteHandler),
    ('/api/login', LoginHandler),
    ('/api/logout', LogoutHandler)

], debug=True)