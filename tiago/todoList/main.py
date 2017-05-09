import webapp2
import json
import datetime
from google.appengine.api import users

from models import *
from utils import *

class BaseHandler(webapp2.RequestHandler):
    pass

class LoginHandler(BaseHandler):
    def get(self):
        user = users.get_current_user()
        if user:
            nickname = user.nickname()
            logout_url = users.create_logout_url('/')
            self.redirect(logout_url)
            
        else:
            login_url = users.create_login_url('/')
            self.redirect(login_url)

# Not complete
class LogoutHandler(BaseHandler):
    def get(self):
        user = users.get_current_user()
        if user:
            logout_url = users.create_logout_url('/')
            self.redirect(logout_url)



app = webapp2.WSGIApplication([
    ('/api/login', LoginHandler),
    ('/api/logout', LogoutHandler),
], debug=True)
