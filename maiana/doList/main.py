from google.appengine.ext import ndb
from utils import *
from models import *

import webapp2
import json

class LoginWebapp(webapp2.RequestHandler):
    
	def get(self):
		user = users.get_current_user()

		if user is None: 

			login_url = users.create_login_url('/')
			self.redirect(login_url)

class LogoutWebapp(webapp2.RequestHandler):
    
	def get(self):
		user = users.get_current_user()

		if user: 			
			logout_url = users.create_logout_url('/')
			self.redirect(logout_url)

class TaskListWebapp(webapp2.RequestHandler):
    
	@is_logged	
	def get(self):

		all_lists = TaskList.query()
		response = [list.to_dict() for list in all_lists]
		self.response.headers['Content-Type'] = 'application/json; charset=utf-8'
		self.response.write(data2json(response))
		
	@is_logged	
	def post(self):
    	
		data = json.loads(self.request.body)
		str_id = data['name'].lower()

		list = TaskList(id=str_id) #definindo o id como nome.
		list.name = data['name']
		
		list.put()
		
		self.response.headers['Content-Type'] = 'application/json; charset=utf-8'
		self.response.write(data2json(list.to_dict()))
      
class ListWebapp(webapp2.RequestHandler):

	@is_logged	
	def get(self, str_id_list):
    		
		str_id = str_id_list.lower()
		list = TaskList.get_by_id(str_id)

		response = [Task.get_by_id(task).to_dict() for task in list.tasks]
		self.response.headers['Content-Type'] = 'application/json; charset=utf-8'
		self.response.write(data2json(response))
		
	@is_logged	
	def post(self, str_id_list):
    	
		str_id = str_id_list.lower()
		list = TaskList.get_by_id(str_id)
		activity = json.loads(self.request.body)
		
		task = Task(id=activity['name']) #definindo o id como nome.
		task.name = activity['name']
		task.comment = activity['comment']
		
		task.put()
		list.tasks.append(task.name)
		list.put()
		
		self.response.headers['Content-Type'] = 'application/json; charset=utf-8'
		self.response.write(data2json(task.to_dict()))

class UserWebapp(webapp2.RequestHandler):
    
	@is_logged
	def get(self):
    		return True

app = webapp2.WSGIApplication([
	('/login', LoginWebapp),
	('/logout', LogoutWebapp),
	('/api/user', UserWebapp),
	('/api', TaskListWebapp),
	('/api/(\w+)/list', ListWebapp)
], debug=True)
