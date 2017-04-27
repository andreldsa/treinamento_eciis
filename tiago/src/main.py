import webapp2
import json
import datetime

from models import *
from utils import *


class InstitutionHandler(webapp2.RequestHandler):
    def get(self):
        query = Institution.query()
        institutionName = self.request.get("name")
        if institutionName:
            query = query.filter(Institution.name == institutionName)
        data = [institution.to_dict() for institution in query]
        self.response.headers['Content-Type'] = 'application/json; charset=utf-8'
        self.response.write(data2json(data))

    def post(self):
        data = json.loads(self.request.body)
        newinstitution = Institution()
        newinstitution.name = data.get('name')
        newinstitution.representativeName = data.get('representativeName')
        newinstitution.cnpj = data.get('cnpj')
        newinstitution.legal_nature = data.get('legal_nature')
        newinstitution.address = data.get('address')
        newuser.description = data.get('description')
        newinstitution.email = data.get('email')
        newinstitution.telephone = data.get('telephone')
        newinstitution.put()
        self.response.write('{"iid": "%d"}' % newinstitution.key.integer_id())
        self.response.set_status(201)


class UserHandler(webapp2.RequestHandler):
    def get(self):
        query = User.query()
        data = [user.to_dict() for user in query]
        self.response.headers['Content-Type'] = 'application/json; charset=utf-8'
        self.response.write(data2json(data))

    def post(self):
        data = json.loads(self.request.body)
        newuser = User()
        newuser.name = data.get('name')
        newuser.password = data.get('password')
        newuser.cpf = data.get('cpf')
        newuser.email = data.get('email')
        newuser.put()
        self.response.write('{"iid:" "%d"}' % newuser.key.integer_id())
        self.response.set_status(201)

class PostHandler(webapp2.RequestHandler):
    def get(self):
        query = Post.query()
        data = [post.to_dict() for post in query]
        self.response.headers['Content-Type'] = 'application/json; charset=utf-8'
        self.response.write(data2json(data))

    def post(self):
        data = json.loads(self.request.body)
        newpost = Post()
        newpost.institution= data.get('institution')
        newpost.author = data.get('author')
        time = data.get('', datetime.datetime.now().isoformat().split(".")[0])
        newpost.time = datetime.datetime.strptime(time, "%Y-%m-%dT%H:%M:%S")
        newpost.likes = data.get('likes')
        newpost.put()
        self.response.write('{"iid:" "%d"}' % newpost.key.integer_id())
        self.response.set_status(201)


app = webapp2.WSGIApplication([
    ('/api/institution.*', InstitutionHandler),
    ('/api/user.*', UserHandler),
    ('/api/post.*', PostHandler),
], debug=True)
