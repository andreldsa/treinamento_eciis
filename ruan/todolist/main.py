import webapp2

from models import *
from utils import *


class BaseHandler(webapp2.RequestHandler):

    # verify if the user has this list
    def verifyListId(self, user, listId):
        lists_ids = [int(key.id()) for key in user.lists]
        if listId not in lists_ids:
            self.response.write(
                ('{"msg":"The user %s does not have this list"}' % user.email).encode('utf-8'))
            self.response.set_status(401)

    # verify if the user has this task
    def verifyTaskId(self, user, listId, taskId):
        verifyListId(user, listId)
        _list = List.get_by_id(listId)
        tasks_ids = [int(key.id()) for key in _list.tasks]
        if taskId not in tasks_ids:
            self.response.write(
                '{"msg":"The user %s does not have this task"}' % user.email)
            self.response.set_status(401)


class LoginHandler(BaseHandler):

    def get(self):
        uri = self.request.get('uri', '/')
        self.redirect(users.create_login_url(uri))


class LogoutHandler(BaseHandler):

    def get(self):
        self.redirect(users.create_logout_url('/'))


class UserHandler(BaseHandler):

    # get user data
    @login_required
    @json_response
    def get(self, user):
        if not user.email:
            user.email = user.key.id()
            user.put()

        user = user.to_dict()
        self.response.write(data2json(user).encode('utf-8'))


class ListHandler(BaseHandler):

    # Get a List by id
    @login_required
    @json_response
    def get(self, user, listId):
        _list = List.get_by_id(int(listId))
        _list = data2dict(_list)
        self.response.write(data2json(_list).encode('utf-8'))

    # Create a list
    @login_required
    @json_response
    def post(self, user):
        data = json.loads(self.request.body)
        list_key = List.create(data)
        user.add_list(list_key)
        newList = data2dict(list_key.get())
        self.response.write(data2json(newList).encode('utf-8'))
        self.response.set_status(201)

    # Delete list
    @login_required
    @json_response
    def delete(self, user, listId):
        _list = List.get_by_id(int(listId))
        List.delete(_list)
        user.remove_list(_list.key)
        _list = data2dict(_list)
        self.response.write(data2json(_list).encode('utf-8'))


class ListCollectionHandler(BaseHandler):

    # Get all user's lists
    @login_required
    @json_response
    def get(self, user):
        lists_keys = user.lists
        lists = [data2dict(key.get()) for key in lists_keys]
        self.response.write(data2json(lists).encode('utf-8'))


class TaskCollectionHandler(BaseHandler):

    # Get all tasks from a list
    @login_required
    @json_response
    def get(self, user, listId):
        _list = List.get_by_id(int(listId))
        tasks = ndb.get_multi(_list.tasks)
        tasks = [data2dict(task) for task in tasks if task is not None]
        self.response.write(data2json(tasks).encode('utf-8'))


class ListTaskHandler(BaseHandler):

    # Get a task from a list by id
    @login_required
    @json_response
    def get(self, listId, taskId):
        task = Task.get_by_id(int(taskId))
        task = data2dict(task)
        self.response.write(data2json(task).encode('utf-8'))

    # Add a new task to a list
    @login_required
    @json_response
    def post(self, user, listId):
        data = json.loads(self.request.body)
        _list = List.get_by_id(int(listId))
        task_key = Task.create(data, _list.key)
        _list.add_task(task_key)
        newTask = data2dict(task_key.get())
        self.response.write(data2json(newTask).encode('utf-8'))
        self.response.set_status(201)

    # Delete task from list
    @login_required
    @json_response
    def delete(self, user, listId, taskId):
        task = Task.get_by_id(int(taskId))
        _list = List.get_by_id(int(listId))
        _list.remove_task(task.key)
        Task.delete(task)
        task = data2dict(task)
        self.response.write(data2json(task).encode('utf-8'))


app = webapp2.WSGIApplication([
    ('/login', LoginHandler),
    ('/logout', LogoutHandler),
    ('/api/users', UserHandler),
    ('/api/list', ListHandler),
    ('/api/lists', ListCollectionHandler),
    ('/api/lists/(\d+)', ListHandler),
    ('/api/lists/(\d+)/task', ListTaskHandler),
    ('/api/lists/(\d+)/tasks', TaskCollectionHandler),
    ('/api/lists/(\d+)/tasks/(\d+)', ListTaskHandler)
], debug=True)
