# -*- coding: utf-8 -*-

import webapp2
import logging

import json

from models import *




class BaseHandler(webapp2.RequestHandler):
    pass


class SEU_HANDLER(BaseHandler):
    pass


class ErroHandler(webapp2.RequestHandler):

    def get(self):
        self.response.write("Rota Inesistente")


class InstitutionMembersHandler(webapp2.RequestHandler):

    def get(self, id):
        institution = Institution.get_by_id(int(id))
        members = institution.members
        list = [member.key.integer_id() for member in members]
        self.response.write(list)

    def post(self, id):
        institution = Institution.get_by_id(int(id))
        data = json.loads(self.request.body)
        user_id = data['id']
        user = User.get_by_id(int(user_id))
        institution.members.append(user)
        institution.put()
        self.response.write(data)


class InstitutionFollowersHandler(webapp2.RequestHandler):

    def get(self, id):
        institution = Institution.get_by_id(int(id))
        followers = institution.followers
        list = [follower.key.integer_id() for follower in followers]
        self.response.write(list)

    def post(self, id):
        institution = Institution.get_by_id(int(id))
        data = json.loads(self.request.body)
        user_id = data['id']
        user = User.get_by_id(int(user_id))
        institution.followers.append(user)
        institution.put()
        self.response.write(data)








app = webapp2.WSGIApplication([
    ("/api/institution", SEU_HANDLER),
    ("/api/institution/:id", SEU_HANDLER),
    ("/api/institution/(\d+)/members", InstitutionMembersHandler),
    ("/api/institution/(\d+)/followers", InstitutionFollowersHandler),
    ("/api/institution/:id/timeline", SEU_HANDLER),
    ("/api/institution/:id/post", SEU_HANDLER),
    ("/api/institution/:id/post/:id", SEU_HANDLER),
    ("/api/institution/:id/post/:id/comments", SEU_HANDLER),
    ("/api/user", SEU_HANDLER),
    ("/api/user/:id", SEU_HANDLER),
    ("/api/user/:id/timeline", SEU_HANDLER),
    ("/api/user/:id/notifications", SEU_HANDLER),
    ("/api/.*", ErroHandler)
], debug=True)
