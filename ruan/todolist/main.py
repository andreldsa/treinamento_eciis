import webapp2

from models import *
from utils import *


class BaseHandler(webapp2.RequestHandler):
    pass



class UserHandler(webapp2.RequestHandler):

    def get(self, userId):
        user = User.get_by_id(int(userId))
        user = data2dict(user)
        self.response.headers['content-type'] = 'application/json; charset=utf-8'
        self.response.write(data2json(user))

    
    def post(self):
        data = json.loads(self.request.body)
        newUser = User()
        newUser.name = data.get('name')
        newUser.email = data.get('email')
        newUser.put()
        newUser = data2dict(newUser)
        self.response.headers['content-type'] = 'application/json; charset=utf-8'
        self.response.write(data2json(newUser))
        


class ListHandler(BaseHandler): 
    # Get a List by id
    def get(self, listId):
        _list = List.get_by_id(int(listId))    
        _list = data2dict(_list)
        self.response.headers['content-type'] = 'application/json; charset=utf-8'
        self.response.write(data2json(_list))
    

    # Create a list
    def post(self):
        data = json.loads(self.request.body)
        newList = List()
        newList.title = data.get('title')
        newList.description = data.get('description')
        newList.put()
        newList = data2dict(newList)
        self.response.headers['content-type'] = 'application/json; charset=utf-8'        
        self.response.write(data2json(newList))
        self.response.set_status(201)



class ListCollectionHandler(BaseHandler):
    # Get all lists
    def get(self):
        query = List.query()
        lists = [data2dict(_list) for _list in query]
        self.response.headers['content-type'] = 'application/json; charset=utf-8'
        self.response.write(data2json(lists))



class TaskHandler(BaseHandler):
    # Get a task by id
    def get(self, taskId):
        task = Task.get_by_id(int(taskId))
        task = data2dict(task)
        self.response.headers['content-type'] = 'application/json; charset=utf-8'        
        self.response.write(data2json(task))



class TaskCollectionHandler(BaseHandler):
    # Get all tasks
    def get(self):
        query = Task.query()
        tasks = [data2dict(task) for task in query]
        self.response.headers['content-type'] = 'application/json; charset=utf-8'
        self.response.write(data2json(tasks))



class ListTasksHandler(BaseHandler):
    # Get all tasks from a list 
    def get(self, listId):
        _list = List.get_by_id(int(listId))
        tasks = ndb.get_multi(_list.tasks)
        # Convert a task to a dictionary and add to a list if not none
        tasks = [data2dict(t) for t in tasks if t]
        self.response.headers['Content-Type'] = 'application/json; charset=utf-8'
        self.response.write(data2json(tasks))
    
    
    # Add a new task to a list
    def post(self, listId):
        # get task data
        data = json.loads(self.request.body)
        # get list by id
        _list = List.get_by_id(int(listId))
        list_key = _list.key
        # create task
        newTask = Task()
        newTask.title = data.get('title')
        newTask.description = data.get('description')
        newTask.priority = data.get('priority')        
        newTask.list = list_key
        # save task
        task_key = newTask.put()
        # add task key to list
        _list.tasks.append(task_key)
        _list.put()

        newTask = data2dict(newTask)
        self.response.headers['content-type'] = 'application/json; charset=utf-8'        
        self.response.write(data2json(newTask))        
        self.response.set_status(201)
    
            


app = webapp2.WSGIApplication([
    ('/api/list', ListHandler),     
    ('/api/list/(\d+)', ListHandler), 
    ('/api/list/(\d+)/task', ListTasksHandler), 
    ('/api/list/(\d+)/tasks', ListTasksHandler), 
    ('/api/lists', ListCollectionHandler), 
    ('/api/task/(\d+)', TaskHandler), 
    ('/api/tasks', TaskCollectionHandler),
    ('/api/users', UserHandler),
    ('/api/users/(\d+)', UserHandler)

], debug=True)
