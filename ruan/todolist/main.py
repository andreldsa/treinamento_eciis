import webapp2

from models import *
from utils import *

from google.appengine.api import users


def login_required(method):
    def check_login(self, *args):
        google_user = users.get_current_user()

        if google_user is None:
            self.response.write('{"msg":"requires authentication", "login_url":"http://%s/login"}' % self.request.host)
            self.response.set_status(401)
            return
        
        user = User.get_or_insert(google_user.email().lower())
        method(self, user, *args)
    
    return check_login


# verify if the user has this list 
def verifyListId(user, listId):
     if listId not in user.lists:
        self.response.write('{"msg":"The user %s does not have this list"}' %user.email)
        self.response.set_status(401)
        return


# verify if the user has this task 
def verifyTaskId(user, listId, taskId):
    verifyListId(user, listId)
    _list = List.get_by_id(listId)
    if taskId not in _list.tasks:
        self.response.write('{"msg":"The user %s does not have this task"}' %user.email)
        self.response.set_status(401)
        return



class BaseHandler(webapp2.RequestHandler):
    pass



class LoginHandler(BaseHandler):
    def get(self):
        uri = self.request.get('uri', '/')
        self.redirect(users.create_login_url(uri))



class LogoutHandler(BaseHandler):
    def get(self):
        self.redirect(users.create_logout_url('/'))



class UserHandler(BaseHandler):
    @login_required
    def get(self, user):
        if not user.email:
            user.email = user.key.id()
            user.put()

        user_data = {
            "email": user.email,
            "user": user.to_dict(),
            "logout_url": "http://%s/logout" % self.request.host
        }
        self.response.headers['Content-Type'] = 'application/json; charset=utf-8'
        self.response.write(data2json(user_data).encode('utf-8'))
        


class ListHandler(BaseHandler): 
    # Get a List by id
    @login_required
    def get(self, user, listId):
        verifyListId(user, listId)
        _list = List.get_by_id(int(listId))    
        _list = data2dict(_list)
        self.response.headers['content-type'] = 'application/json; charset=utf-8'
        self.response.write(data2json(_list).encode('utf-8'))
    

    # Create a list
    @login_required
    def post(self, user):
        # get list data
        data = json.loads(self.request.body)
        newList = List()
        newList.title = data.get('title')
        newList.description = data.get('description')
        list_key = newList.put()
        # add the list to the user
        user.lists.append(list_key)
        newList = data2dict(newList)
        self.response.headers['content-type'] = 'application/json; charset=utf-8'        
        self.response.write(data2json(newList).encode('utf-8'))
        self.response.set_status(201)


    #TODO  create delete method


class ListCollectionHandler(BaseHandler):
    # Get all user's lists
    @login_required
    def get(self, user):
        lists_keys = user.lists
        # create a collection of lists
        lists = [data2dict(key.get()) for key in lists_keys]
        self.response.headers['content-type'] = 'application/json; charset=utf-8'
        self.response.write(data2json(lists).encode('utf-8'))



class TaskCollectionHandler(BaseHandler):
    # Get all tasks from a list 
    @login_required
    def get(self, user, listId):
        verifyListId(user, listId)
        _list = List.get_by_id(int(listId))
        # get all tasks from this list
        tasks = ndb.get_multi(_list.tasks)
        # Convert a task to a dictionary and add to a list if not none
        tasks = [data2dict(task) for task in tasks if task is not None]
        self.response.headers['Content-Type'] = 'application/json; charset=utf-8'
        self.response.write(data2json(tasks).encode('utf-8'))



class ListTasksHandler(BaseHandler):
    # Get a task from a list by id 
    @login_required
    def get(self, listId, taskId):
        verifyTaskId(user, listId, taskId)
        task = Task.get_by_id(int(taskId))
        task = data2dict(task)
        self.response.headers['content-type'] = 'application/json; charset=utf-8'        
        self.response.write(data2json(task).encode('utf-8'))
    
    
    # Add a new task to a list
    @login_required
    def post(self, user, listId):
        verifyListId(user, listId)
        # get task data
        data = json.loads(self.request.body)
        _list = List.get_by_id(int(listId))
        newTask = Task()
        newTask.title = data.get('title')
        newTask.description = data.get('description')
        newTask.priority = data.get('priority')        
        newTask.list = _list.key
        task_key = newTask.put()
        # add task key to list
        _list.tasks.append(task_key)
        _list.put()
        newTask = data2dict(newTask)
        self.response.headers['content-type'] = 'application/json; charset=utf-8'        
        self.response.write(data2json(newTask).encode('utf-8'))        
        self.response.set_status(201)


    #TODO create delete method
    
            


app = webapp2.WSGIApplication([
    ('/login', LoginHandler),     
    ('/logout', LogoutHandler),     
    ('/api/users', UserHandler),
    ('/api/list', ListHandler),     
    ('/api/lists', ListCollectionHandler), 
    ('/api/lists/(\d+)', ListHandler), 
    ('/api/lists/(\d+)/task', ListTasksHandler),
    ('/api/lists/(\d+)/tasks', TaskCollectionHandler), 
    ('/api/lists/(\d+)/tasks/(\d+)', ListTasksHandler)
], debug=True)