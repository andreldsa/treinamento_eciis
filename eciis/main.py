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

    #This method return the comments of post informed
    def get(self, id_institution, id_post):

        post = Post.get_by_id(int(id_post))
        all_comments = post.comments #Array of comments, how i convert for JSON ?
		

        self.response.write(all_comments)

    def post(self, id_institution, id_post):
		
		data = self.request.body()
		
		post = Post.get_by_id(int(id_post))
        comments = post.comments # Array of JSON
        
        if(not comments):
			comments = []
		
		comments.append(data)      
     
    def patch(self, id_institution, id_post):
		
		data = json.loads(self.request.body)
		index = data.indice
		
		post = Post.get_by_id(int(id_post))
        comments = post.comments
		
		comment = comments[indice]
		
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
		
        

class ErroHandler(webapp2.RequestHandler):

    def get(self):
        self.response.write("Rota Inesistente")

app = webapp2.WSGIApplication([
    ("/api/institution", SEU_HANDLER),
    ("/api/institution/:id", SEU_HANDLER),
    ("/api/institution/:id/members", SEU_HANDLER),
    ("/api/institution/:id/followers", SEU_HANDLER),
    ("/api/institution/:id/timeline", TimelineInstitutionHandler),
    ("/api/institution/:id/post", SEU_HANDLER),
    ("/api/institution/:id/post/:id", SEU_HANDLER),
    ("/api/institution/:id/post/:id/comments", CommentsHandler),
    ("/api/user", SEU_HANDLER),
    ("/api/user/:id", SEU_HANDLER),
    ("/api/user/:id/timeline", SEU_HANDLER),
    ("/api/user/:id/notifications", SEU_HANDLER),
    ("/api/.*", ErroHandler)
], debug=True)
