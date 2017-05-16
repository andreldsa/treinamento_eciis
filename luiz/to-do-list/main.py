import webapp2
import sys
import logging

sys.path.append("model")
sys.path.append("util")

import models
import util


class BaseHandler(webapp2.RequestHandler):
    def handle_exception(self, exception, debug):
        if isinstance(exception, util.AuthorizationExeption):
            self.response.write('{"msg":"requires authentication", "login_url":"http://%s/login"}' % self.request.host)
            self.response.set_status(401)
        else:
            logging.error(str(exception))
            self.response.write("oops! %s\n" % str(exception))


class TaskHandler(BaseHandler):
    @util.login_required
    def get(self):
        user_email = util.current_user_email()
        userData = models.User.get_by_email(user_email)
        data = userData.get_tasks()

        self.response.headers['Content-Type'] = 'application/json; charset=utf-8'
        self.response.write(util.data2json(data).encode('utf-8'))

    @util.login_required
    def post(self):
        data = util.json2data(self.request.body)
        task_key = models.Task.createTask(data['name_task'])

        user_email = util.current_user_email()
        userData = models.User.get_by_email(user_email)
        userData.tasks.append(task_key)
        userData.put()

        self.response.set_status("201")
        self.response.headers['Content-Type'] = 'application/json; charset=utf-8'
        self.response.write(util.data2json(task_key.get().to_dict()).encode('utf-8'))


class UserHandler(BaseHandler):
    @util.login_required
    def get(self):
        user_email = util.current_user_email()
        user = models.User.get_or_insert_by_email(user_email)
        user_data = {
            "email": user.email,
            "logout_url": "https://%s/logout" % self.request.host,
            "gravatar_url": user.gravatar_url
        }

        self.response.headers['Content-Type'] = 'application/json; charset=utf-8'
        self.response.write(util.data2json(user_data).encode('utf-8'))


class LoginHandler(BaseHandler):
    def get(self):
        login_url = util.login()
        self.redirect(login_url)


class LogoutHandler(BaseHandler):
    @util.login_required
    def get(self):
        logout_url = util.logout()
        self.redirect(logout_url)


app = webapp2.WSGIApplication([
    ("/api", UserHandler),
    ("/api/todo", TaskHandler),
    ("/login", LoginHandler),
    ("/logout", LogoutHandler),
], debug=True)
