import webapp2

from google.appengine.api import users


class BaseHandler(webapp2.RequestHandler):

    @staticmethod
    def isLoggedIn(func):
        def checkLoggedIn(self):
            user = users.get_current_user()
            if user:
                nickname = user.nickname()
                logout_url = users.create_logout_url('/api')
                greeting = 'Welcome, {}! (<a href="{}">sign out</a>)'.format(
                    nickname, logout_url)
            else:
                login_url = users.create_login_url('/api')
                greeting = '<a href="{}">Sign in</a>'.format(login_url)

            self.response.write(
                '<html><body>{}</body></html>'.format(greeting))
            return func(self)
        return checkLoggedIn


class Handler(BaseHandler):

    @BaseHandler.isLoggedIn
    def get(self):
        pass

app = webapp2.WSGIApplication([
    (".*", Handler)
])
