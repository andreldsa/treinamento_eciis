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

    def post(self):
        data = json2data(self.request.body)
        task = Task.createTask(data['name_task'])

        self.response.set_status("201")
        self.response.headers['Content-Type'] = 'application/json; charset=utf-8'
        self.response.write(data2json(task.to_dict()))

app = webapp2.WSGIApplication([
    ("/api/todo", TaskHandler),
], debug=True)
