import webapp2

from model import User
from model import Task

import json

from utils import *
from google.appengine.api import users


class LoginHandler(webapp2.RequestHandler):

    def get(self):
        self.redirect(users.create_login_url('/'))


class LogoutHandler(webapp2.RequestHandler):

    def get(self):
        user = users.get_current_user()
        if user:
            self.redirect(users.create_logout_url(''))



class Handler(webapp2.RequestHandler):

    def get(self):
        user_google = users.get_current_user()
        if user_google is None:
            self.response.set_status(401)
            self.response.headers['Content-Type'] = 'application/json; charset=utf-8'
            self.response.write('{"msg": "erro de autenticacao"}')
        else:
            user_email = user_google.email()
            user = User.get_or_insert(user_email, email=user_email)
            user_tasks = [task.get().to_dict() for task in user.tasks]
            self.response.headers['Content-Type'] = 'application/json; charset=utf-8'
            self.response.write(data2json(user_tasks).encode('utf-8'))


    def post(self):
        user_google = users.get_current_user()
        if user_google is None:
            self.response.set_status(401)
            self.response.headers['Content-Type'] = 'application/json; charset=utf-8'
            self.response.write('{"msg": "erro de autenticacao"}')
        else:
            user_email = user_google.email()
            user = User.get_or_insert(user_email, email=user_email)
            data = json.loads(self.request.body)
            task = Task()
            task.name = data['name']
            task.description = data['description']
            task_key = task.put()
            user.tasks.append(task_key)
            user.put()
            self.response.headers['Content-Type'] = 'application/json'
            self.response.set_status(201)


app = webapp2.WSGIApplication([
    ('/api/tasks', Handler),
    ('/api/login', LoginHandler),
    ('/api/logout', LogoutHandler)

], debug=True)