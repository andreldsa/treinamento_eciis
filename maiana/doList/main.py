from google.appengine.ext import ndb
from utils import *

import webapp2
import json

class Task(ndb.Model):
	name = ndb.StringProperty(required=True)
	date_created = ndb.DateTimeProperty(auto_now_add=True)
	status = ndb.BooleanProperty(default=False)
	comment = ndb.TextProperty()

    
	
class ListWebapp(webapp2.RequestHandler):

	#@is_logged    	
	def get(self):

		all_task = Task.query()
		response = [task.to_dict() for task in all_task]
		self.response.headers['Content-Type'] = 'application/json; charset=utf-8'
		self.response.write(data2json(response))

	def post(self):
    	
		activity = json.loads(self.request.body)

		task = Task(id=activity['name']) #definindo o id como nome.
		task.name = activity['name']
		task.comment = activity['comment']
		
		task.put()
		
		self.response.headers['Content-Type'] = 'application/json; charset=utf-8'
		self.response.write(data2json(task.to_dict()))
      
     
	def patch(self):
		
		name_request = self.request.get('nome')
		
		task = Task.get_by_id(name_request)
		task.status = True
		
		task.put()


app = webapp2.WSGIApplication([
	('/api', ListWebapp)
], debug=True)
