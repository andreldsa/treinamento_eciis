import webapp2

from model import Usuario
from model import Task

import json

from utils import *
from google.appengine.api import users


class LoginHandler(webapp2.RequestHandler):

    def get(self):
        guser = users.get_current_user()
        if guser is None:
            self.redirect(users.create_login_url('/'))


class LogoutHandler(webapp2.RequestHandler):

    def get(self):
        guser = users.get_current_user()
        if guser:
            self.redirect(users.create_logout_url(''))



class Handler(webapp2.RequestHandler):

    def get(self):
        query = Task.query()
        tasks = [task.to_dict() for task in query]
        self.response.headers['Content-Type'] = 'application/json; charset=utf-8'
        self.response.write(data2json(tasks))


    def post(self):
        data = json.loads(self.request.body)
        self.response.write(data)
        task = Task()
        task.name = data['name']
        task.description = data['description']
        task.put()
        self.response.headers['Content-Type'] = 'application/json'
        self.response.set_status(201)


app = webapp2.WSGIApplication([
    ('/api/tasks', Handler),
    ('/api/login', LoginHandler),
    ('/api/logout', LogoutHandler)

], debug=True)