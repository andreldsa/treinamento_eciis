import webapp2
from models import *
import json
import datetime
from utils import *


class InstitutionHandler(webapp2.RequestHandler):

    def get(self):
        query = Institution.query()
        data =   [institution.to_dict() for institution in query]
        self.response.headers['Content-Type'] = 'application/json; charset=utf-8'
        self.response.write(data2json(data))

    def post(self):
        data = json.loads(self.request.body)
        institution = Institution()
        institution.name = data['name']
        institution.reponsable_name = data['responsable_name']
        institution.cnpj = data['cnpj']
        institution.nature = data['nature']
        institution.adress = data['adress']
        institution.field_of_work = data['field_of_work']
        institution.description = data['description']
        institution.email = data['email']
        institution.phone = data['phone']
        institution.put()
        self.response.write('{"iid": "%d"}' % institution.key.integer_id())
        self.response.set_status(201)


class UserHandler(webapp2.RequestHandler):

    def get(self):
        query = User.query()
        data = [user.to_dict() for user in query]
        self.response.headers['Content-Type'] = 'application/json; charset=utf-8'
        self.response.write(data2json(data))

    def post(self):
        data = json.loads(self.request.body)
        user = User()
        user.name = data['name']
        user.password = data['password']
        user.cpf = data['cpf']
        user.email = data['email']
        user.put()
        self.response.write('{"iid": "%d"}' % user.key.integer_id())
        self.response.set_status(201)


class PostHandler(webapp2.RequestHandler):

    def get(self):
        query = Post.query()
        data = [post.to_dict() for post in query]
        self.response.headers['Content-Type'] = 'application/json; charset=utf-8'
        self.response.write(data2json(data))


    def post(self):
        data = json.loads(self.request.body)
        post = Post()
        post.institution_name = data['institution_name']
        post.author_name = data['author_name']
        post.likes = data['likes']
        date = data.get('date', datetime.datetime.now().isoformat().split(".")[0])
        post.date = datetime.datetime.strptime(date, "%Y-%m-%dT%H:%M:%S")
        post.put()
        self.response.write('{"iid": "%d"}' % post.key.integer_id())
        self.response.set_status(201)


app = webapp2.WSGIApplication([
    ('/api/institution', InstitutionHandler), 
    ('/api/user', UserHandler), 
    ('/api/post', PostHandler)
], debug = True)