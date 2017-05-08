import webapp2
from model import *
import json
import datetime
from utils import *
from google.appengine.api import users


class Handler(webapp2.RequestHandler):

    def get(self):
        user = users.get_current_user()
        if user:
            query = Task.query(Task.id_user == user.user_id())
            data = [todo.to_dict() for todo in query]
            self.response.headers['Content-Type'] = 'application/json; charset=utf-8'
            self.response.write(data2json(data))
        else:
            url = users.create_login_url(self.request.uri)
            url_linktext = 'Login'

    def post(self):
        user = users.get_current_user()
        if user:
            data = json.loads(self.request.body)
            task = Task()
            task.name = data['name']
            task.id_user = user.user_id()
            task.put()
            self.response.set_status(201)
        else:
            url = users.create_login_url(self.request.uri)
            url_linktext = 'Login'


app = webapp2.WSGIApplication([
    ('/api/tasks.*', Handler)
], debug = True)