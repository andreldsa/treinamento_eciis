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


class ListWebapp(webapp2.RequestHandler):

    @is_logged
    def get(self, user_email):
        user = User.get_by_id(user_email)
        all_lists = user.lists

        response = [List.get_by_id(list.id()).to_dict() for list in all_lists]
        self.response.headers[
            'Content-Type'] = 'application/json; charset=utf-8'
        self.response.write(data2json(response))

    @is_logged
    def post(self, user_email):
        user = User.get_by_id(user_email)
        data = json.loads(self.request.body)

        list = List()
        list.name = data['name']
        list.put()

        user.add_list(list.key)
        user.put()

        self.response.headers[
            'Content-Type'] = 'application/json; charset=utf-8'
        self.response.write(data2json(dict_json(list)))

    @is_logged
    def delete(self, user_email, id_list):
        user = User.get_by_id(user_email)

        list = List.get_by_id(int(id_list))
        list.key.delete()

        user.remove_list(list.key)
        user.put()
        self.response.headers[
            'Content-Type'] = 'application/json; charset=utf-8'
        self.response.write(data2json(list.to_dict()))


class TaskWebapp(webapp2.RequestHandler):

    @is_logged
    def get(self, user, id_list):

        list = List.get_by_id(int(id_list))
        response = [dict_json(Task.get_by_id(task.id())) for task in list.tasks]
        self.response.headers[
            'Content-Type'] = 'application/json; charset=utf-8'
        self.response.write(data2json(response))

    @is_logged
    def post(self, user, id_list):

        list = List.get_by_id(int(id_list))
        activity = json.loads(self.request.body)

        task = Task()
        task.name = activity['name']
        task.comment = activity.get('comment')

        task.put()
        list.add_task(task.key)
        list.put()

        self.response.headers[
            'Content-Type'] = 'application/json; charset=utf-8'
        self.response.write(data2json(dict_json(task)))

    @is_logged
    def put(self, user, id_list):

        activity = json.loads(self.request.body)

        task = Task.get_by_id(activity)
        task.status = True
        task.put()

        self.response.headers[
            'Content-Type'] = 'application/json; charset=utf-8'
        self.response.write(data2json(dict_json(task)))

    @is_logged
    def delete(self, user_email, id_list, id_task):

        task = Task.get_by_id(int(id_task))
        task.key.delete()

        list = List.get_by_id(int(id_list))
        list.remove_task(task.key)
        list.put()

        self.response.headers[
            'Content-Type'] = 'application/json; charset=utf-8'
        self.response.write(data2json(dict_json(task)))


class UserWebapp(webapp2.RequestHandler):

    @is_logged
    def get(self, user_email):
        user=User.get_by_id(user_email)

        if(user is None):
            user=User.insert(user_email)

        perfil=user.to_dict()
        perfil=get_list(perfil)
        self.response.headers[
            'Content-Type']='application/json; charset=utf-8'
        self.response.write(data2json(perfil))

app = webapp2.WSGIApplication([
    ('/login', LoginWebapp),
    ('/logout', LogoutWebapp),
    ('/api', UserWebapp),
    ('/api/list', ListWebapp),
    ('/api/list/(\w+)', ListWebapp),
    ('/api/(\w+)/list', TaskWebapp),
    ('/api/(\w+)/(\w+)', TaskWebapp)
], debug=True)
