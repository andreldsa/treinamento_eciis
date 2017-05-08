import webapp2
from model import *
import json
import datetime
from utils import *




class Handler(webapp2.RequestHandler):

    def get(self):
        query = Task.query()
        data = [todo.to_dict() for todo in query]
        self.response.headers['Content-Type'] = 'application/json; charset=utf-8'
        self.response.write(data2json(data))

    def post(self):
        data = json.loads(self.request.body)
        task = Task()
        task.name = data['name']
        task.put()
        self.response.set_status(201)


app = webapp2.WSGIApplication([
    ('/api/tasks.*', Handler)
], debug = True)