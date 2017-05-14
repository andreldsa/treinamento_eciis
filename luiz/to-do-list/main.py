import webapp2
import sys

sys.path.append("model")
sys.path.append("util")

from models import *
from util import *

class BaseHandler(webapp2.RequestHandler):
    def handle_exception(self, exception, debug):
        if isinstance(exception, AuthorizationExeption):
            self.response.write('{"msg":"requires authentication", "login_url":"http://%s/login"}' % self.request.host)
            self.response.set_status(401)
        else:
            logging.error(str(exception))
            self.response.write("oops! %s\n" % str(exception))

class TaskHandler(BaseHandler):
    @login_required
    def get(self, user):
        userData = User.get_by_email(user.email().lower())
        data = userData.get_tasks()

        self.response.headers['Content-Type'] = 'application/json; charset=utf-8'
        self.response.write(data2json(data).encode('utf-8'))

    @login_required
    def post(self, user):
        data = json2data(self.request.body)
        task_key = Task.createTask(data['name_task'])

        userData = User.get_by_email(user.email().lower())
        userData.tasks.append(task_key)
        userData.put()

        self.response.set_status("201")
        self.response.headers['Content-Type'] = 'application/json; charset=utf-8'
        self.response.write(data2json(task_key.get().to_dict()).encode('utf-8'))

class UserHandler(BaseHandler):
    @login_required
    def get(self, user):
        user = current_user();
        user_data = {
            "email": user.email,
            "logout_url": "https://%s/logout" % self.request.host,
            "gravatar_url": user.gravatar_url
        }

        self.response.headers['Content-Type'] = 'application/json; charset=utf-8'
        self.response.write(data2json(user_data).encode('utf-8'))

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
    ("/api", UserHandler),
    ("/api/todo", TaskHandler),
    ("/login", LoginHandler),
    ("/logout", LogoutHandler),
], debug=True)
