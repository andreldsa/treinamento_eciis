# -*- coding: utf-8 -*-

import webapp2
import logging

import json

from models import *


class BaseHandler(webapp2.RequestHandler):
    pass


class SEU_HANDLER(BaseHandler):
    pass

class institutionHandler(BaseHandler):

    def get(self, institutionId):
        id = int(institutionId)
        data = Intitution.get_by_id(id)
        self.response.headers['Content-Type'] = 'application/json; charset=utf-8'
        self.response.write(data2json(data))


    def post(self):
        data = json.loads(self.request.body)
        newInstitution = Institution()
        newInstitution.admin = User()
        newInstitution.parent_institution = data.get('parent_institution')
        newInstitution.state = data.get('state')
        newInstitution.put()
        self.response.set_status(201)


    def patch(self):



    def delete(self, institutionId):
        id = int(institutionId)
        institution = Intitution.get_by_id(id)
        institution.state = 'inactive'
        institution.put()


class ErroHandler(webapp2.RequestHandler):

    def get(self):
        self.response.write("Rota Inesistente")

class InstitutionPostHandler(webapp2.RequestHandler):

	def get(self, institution_id, post_id):

                post = Post.get_by_id(int(post_id))
                self.response.write(post)

            def patch(self):
                pass

            def delete(self):

                post = Post.get_by_id(int(post_id))

                post.state = 'deleted'
                post.put()

class UserNotifications(webapp2.RequestHandler):

    def get(self, user_id):

        user = User.get_by_id(int(user_id))
        notifications = user.notifications

        self.response.write(notifications)



app = webapp2.WSGIApplication([
    ("/api/institution", institutionHandler),
    ("/api/institution/:id", institutionHandler),
    ("/api/institution/:id/members", SEU_HANDLER),
    ("/api/institution/:id/followers", SEU_HANDLER),
    ("/api/institution/:id/timeline", SEU_HANDLER),
    ("/api/institution/:id/post", SEU_HANDLER),
    ("/api/institution/(\d+)/post/(\d+)", InstitutionPostHandler),
    ("/api/institution/:id/post/:id/comments", SEU_HANDLER),
    ("/api/user", SEU_HANDLER),
    ("/api/user/:id", SEU_HANDLER),
    ("/api/user/:id/timeline", SEU_HANDLER),
    ("/api/user/(\d+)/notifications", UserNotifications),
    ("/api/.*", ErroHandler)
], debug=True)
