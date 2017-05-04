# -*- coding: utf-8 -*-

import webapp2
import logging

import json

from models import *


class BaseHandler(webapp2.RequestHandler):
    pass


class SEU_HANDLER(BaseHandler):
    pass

class CommentsHandler(BaseHandler):
    
     #Util
    def date_handler(obj):
        if hasattr(obj, 'isoformat'):
            return obj.isoformat()
        elif hasattr(obj, 'email'):
            return obj.email()

        return obj

    def data2json(data):
        return json.dumps(
        data,
        default=date_handler,
        indent=2,
        separators=(',', ': '),
        ensure_ascii=False
    )

    #This method return the comments of post informed
    def get(self, id_institution, id_post):

        post = Post.get_by_id(int(id_post))
        all_comments = post.comments #Array of comments, how i convert for JSON ?	

        self.response.headers['Content-Type'] = 'application/json; charset=utf-8'
        self.response.write(data2json(all_comments))

    def post(self, id_institution, id_post):
		
        data = self.request.body()
		
        post = Post.get_by_id(int(id_post))
        comments = post.comments
        
        if(not comments):
            comments = []
		
        comments.append(data)
        self.response.write(data)
      
     
    def patch(self, id_institution, id_post):
		
        data = json.loads(self.request.body)
        index = data.indice
		
        post = Post.get_by_id(int(id_post))
        comments = post.comments
		
        comment = comments[index]
		
        pass
		

class TimelineInstitutionHandler(BaseHandler):
	
     #Util
    def date_handler(obj):
        if hasattr(obj, 'isoformat'):
            return obj.isoformat()
        elif hasattr(obj, 'email'):
            return obj.email()

        return obj

    def data2json(data):
        return json.dumps(
        data,
        default=date_handler,
        indent=2,
        separators=(',', ': '),
        ensure_ascii=False
    )
	
    def get(self, id_institution):
		
        institution = Institution.get_by_id(id_institution)
        timeline = institution.timeline
		
        self.response.headers['Content-Type'] = 'application/json; charset=utf-8'
        self.response.write(data2json(timeline))
		
class InstitutionHandler(BaseHandler):

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
        pass


    def delete(self, institutionId):
        id = int(institutionId)
        institution = Intitution.get_by_id(id)
        institution.state = 'inactive'
        institution.put()

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


class InstitutionPostHandler(BaseHandler):

    def get(self, institution_id, post_id):

        post = Post.get_by_id(int(post_id))
        self.response.write(post)

    def patch(self):
        pass

    def delete(self, institution_id, post_id):

        post = Post.get_by_id(int(post_id))

        post.state = 'deleted'
        post.put()

class UserNotificationsHandler(BaseHandler):

    def get(self, user_id):

        user = User.get_by_id(int(user_id))
        notifications = user.notifications

        self.response.write(notifications)


class UserHandler(BaseHandler):

    def get(self, userId):

        id = int(userId)
        user = User.get_by_id(id)
        self.response.headers['Content-Type'] = 'application/json; charset=utf-8'
        self.response.write(data2json(user))

    def post(self):

        data = json.loads(self.request.body)
        newuser = User()
        newuser.institutions = data.get('institution')
        newuser.state = data.get('state')
        newuser.put()
        self.response.set_status(201)

    def delete(self, userId):

        id = int(userId)
        user = User.get_by_id(id)
        user.state = 'inactive'
        user.put()

    def patch(self):
        pass


class UserTimelineHandler(BaseHandler):

    def get(self, id):

        user = User.get_by_id(int(id))
        posts = user.timeline
        list = [posts.key.integer_id() for posts in posts]
        self.response.headers['Content-Type'] = 'application/json; charset=utf-8'
        self.response.write(list)

app = webapp2.WSGIApplication([
    ("/api/institution", SEU_HANDLER),
    ("/api/institution/(\d+)", TimelineInstitutionHandler),
    ("/api/institution/(\d+)/members", InstitutionMembersHandler),
    ("/api/institution/(\d+)/followers", InstitutionFollowersHandler),
    ("/api/institution", InstitutionHandler),
    ("/api/institution/:id", InstitutionHandler),
    ("/api/institution/:id/members", SEU_HANDLER),
    ("/api/institution/:id/followers", SEU_HANDLER),
    ("/api/institution/:id/timeline", TimelineInstitutionHandler),
    ("/api/institution/:id/post", SEU_HANDLER),
    ("/api/institution/(\d+)/post/(\d+)", InstitutionPostHandler),
    ("/api/institution/(\d+)/post/(\d+)/comments", CommentsHandler),
    ("/api/user", UserHandler),
    ("/api/user/(\d+)", UserHandler),
    ("/api/user/(\d+)/timeline", UserTimelineHandler),
    ("/api/user/(\d+)/notifications", UserNotificationsHandler),
    ("/api/.*", ErroHandler)
], debug=True)
