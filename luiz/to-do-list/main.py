import webapp2
import sys

sys.path.append("model")
sys.path.append("util")

from models import Task
from util import *

class TaskHandler(webapp2.RequestHandler):

    @isLoggedIn
    def get(self):
        data = Task.getAllTasks()

        self.response.headers['Content-Type'] = 'application/json; charset=utf-8'
        self.response.write(data2json(data))

    @isLoggedIn
    def post(self):
        data = json2data(self.request.body)
        task = Task.createTask(data['name_task'])

        self.response.set_status("201")
        self.response.headers['Content-Type'] = 'application/json; charset=utf-8'
        self.response.write(data2json(task.to_dict()))

class LoginHandler(webapp2.RequestHandler):
    def get(self):
        login_url = login()
        self.redirect(login_url)

class LogoutHandler(webapp2.RequestHandler):
    def get(self):
        logout_url = logout()
        self.redirect(logout_url)

app = webapp2.WSGIApplication([
    ("/api/todo", TaskHandler),
    ("/api/login", LoginHandler),
    ("/api/logout", LogoutHandler),
], debug=True)
