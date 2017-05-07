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
        self.response.write(data2json(_list))
    

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
        self.response.write(data2json(task))


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
        tasksKeys = _list.tasks
        tasks = [key.get().to_dict() for key in tasksKeys]
        self.response.headers['Content-Type'] = 'application/json; charset=utf-8'
        self.response.write(data2json(tasks))
    

    # Add a new task to a list
    def post(self, listId):
        data = json.loads(self.request.body)
        _list = List.get_by_id(int(listId))
        listKey = _list.Key()
        newTask = Task()
        newTask.title = data.get('title')
        newTask.description = data.get('description')
        newTask.done = data.get('done')
        newTask.priority = data.get('priority')        
        newTask.list = listKey
        newTask.put()
        self.response.set_status(201)
        


app = webapp2.WSGIApplication([
    ('/api/list', ListHandler), 
    ('/api/list/(\d+)', ListHandler), 
    ('/api/lists', ListsHandler), 
    ('/api/list/(\d+)/task', ListTasksHandler), 
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