import webapp2
import sys

sys.path.append("model")
sys.path.append("util")

from models import *
from util import *

class BaseHandler(webapp2.RequestHandler):
    def handle_exception(self, exception, debug):
        if isinstance(exception, AuthorizationExeption):
            print exception.message
            webapp2.abort(401, str(exception))

        logging.error(str(exception))
        self.response.write("oops! %s\n" % str(exception))

class TaskHandler(BaseHandler):

    @login_required
    def get(self, user):
        userData = User.get_by_email(user.email().lower())
        data = userData.get_tasks()

        self.response.headers['Content-Type'] = 'application/json; charset=utf-8'
        self.response.write(data2json(data))

    @login_required
    def post(self, user):
        data = json2data(self.request.body)
        task_key = Task.createTask(data['name_task'])

        userData = User.get_by_email(user.email().lower())
        userData.tasks.append(task_key)
        userData.put()

        self.response.set_status("201")
        self.response.headers['Content-Type'] = 'application/json; charset=utf-8'
        self.response.write(data2json(task_key.get().to_dict()))

class LoginHandler(BaseHandler):
    def get(self):
        login_url = login()
        self.redirect(login_url)

class LogoutHandler(BaseHandler):
    @login_required
    def get(self, user):
        logout_url = logout()
        self.redirect(logout_url)

app = webapp2.WSGIApplication([
    ("/api/todo", TaskHandler),
    ("/login", LoginHandler),
    ("/logout", LogoutHandler),
], debug=True)
