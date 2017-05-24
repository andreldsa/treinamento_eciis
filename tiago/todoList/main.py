# -*- coding: utf-8 -*-
"""Main."""

import webapp2
import json
import logging
from google.appengine.api import users
from models import User
from models import Task
from utils import data2json


def _assert(condition, status_code, msg):
    """Assert."""
    if condition:
        return

    logging.info("assertion failed: %s" % msg)
    webapp2.abort(status_code, msg)


class BaseHandler(webapp2.RequestHandler):
    """Base handler."""

    pass


class LoginHandler(BaseHandler):
    """Login handler."""

    def get(self):
        """Handle GET request."""
        uri = self.request.get('uri', '/')
        self.redirect(users.create_login_url(uri))


class LogoutHandler(BaseHandler):
    """Logou handler."""

    def get(self):
        """Handle GET request."""
        self.redirect(users.create_logout_url('/'))


def login_required(method):
    """Decorator."""
    def check_login(self, *args):
        user = users.get_current_user()
        if user is None:
            self.response.write(
                '{"msg":"requires authentication", \
                "login_url":"http://%s/login"}' % self.request.host)
            self.response.set_status(401)
            return

        method(self, user, *args)

    return check_login


class MainHandler(BaseHandler):
    """Main."""

    @login_required
    def get(self, user):
        """Handle GET request."""
        current_user = User.get_or_insert(user.email(), id=user.email())
        current_user.put()
        user_data = current_user.get_data()
        user_data["logout_url"] = "http://%s/logout" % self.request.host
        self.response.headers[
            'Content-Type'] = 'application/json; charset=utf-8'
        self.response.write(data2json(user_data).encode('utf-8'))


class UpdateHandler(BaseHandler):
    """Update handler."""

    def put(self, email):
        """Handle PUT request."""
        user = User.get_by_id(email)
        _assert(user, 400, "user not found")
        data = json.loads(self.request.body)
        update = user.update(data)
        self.response.headers[
            'Content-Type'] = 'application/json; charset=utf-8'
        self.response.write(data2json(update).encode('utf-8'))


class DeadlineHandler(BaseHandler):
    """Deadline handle."""

    def get(self):
        """Handle GET request."""
        tasks = Task.query()
        for task in tasks:
            task.verify_deadline()

        users = User.query()
        for user in users:
            user.send_email()

app = webapp2.WSGIApplication([
    ('/login', LoginHandler),
    ('/logout', LogoutHandler),
    ('/api', MainHandler),
    ('/api/update/(.*)', UpdateHandler),
    ('/api/deadline', DeadlineHandler),
], debug=True)
