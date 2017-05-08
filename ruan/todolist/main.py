import webapp2

from models import *
from utils import *


class BaseHandler(webapp2.RequestHandler):
    pass



class ListHandler(BaseHandler): 
    # Get a List by id
    def get(self, listId):
        _list = List.get_by_id(int(listId))    
        self.response.headers['content-type'] = 'application/json; charset=utf-8'
        self.response.write(data2json(_list.to_dict()))
    

    # Create a list
    def post(self):
        data = json.loads(self.request.body)
        newList = List()
        newList.title = data.get('title')
        newList.description = data.get('description')
        newList.put()
        self.response.set_status(201)



class ListsHandler(BaseHandler):
    # Get all lists
    def get(self):
        query = List.query()
        lists = [_list.to_dict() for _list in query]
        self.response.headers['content-type'] = 'application/json; charset=utf-8'
        self.response.write(data2json(lists))



class TaskHandler(BaseHandler):
    # Get a task by id
    def get(self, taskId):
        task = Task.get_by_id(int(taskId))
        self.response.headers['content-type'] = 'application/json; charset=utf-8'        
        self.response.write(data2json(task.to_dict()))



class TasksHandler(BaseHandler):
    # Get all tasks
    def get(self):
        query = Task.query()
        tasks = [task.to_dict() for task in query]
        self.response.headers['content-type'] = 'application/json; charset=utf-8'
        self.response.write(data2json(tasks))



class ListTasksHandler(BaseHandler):
    
    # Get all tasks from a list 
    def get(self, listId):
        _list = List.get_by_id(int(listId))
        tasks = ndb.get_multi(_list.tasks)
        # Convert a task to a dictionary and add to a list if not none
        tasks = [t.to_dict() for t in tasks if t]
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
        task_key = newTask.put()
        
        # add task key to list
        _list.tasks.append(task_key)
        _list.put()
        self.response.set_status(201)
    
            


app = webapp2.WSGIApplication([
    ('/api/list/(\d+)', ListHandler), 
    ('/api/list', ListHandler), 
    ('/api/lists', ListsHandler), 
    ('/api/list/(\d+)/task', ListTasksHandler), 
    ('/api/list/(\d+)/tasks', ListTasksHandler), 
    ('/api/task/(\d+)', TaskHandler), 
    ('/api/tasks', TasksHandler)
], debug=True)



#lists
#   get all lists
#   get a list by id
#   create a list
#

#tasks
#   get all tasks
#

#lists-tasks
#   get all tasks from a list
#   get a task from list
#   add a task to a list
#