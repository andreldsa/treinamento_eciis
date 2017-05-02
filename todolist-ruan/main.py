import webapp2

from models import *
from utils import *


class InstituteHandler(webapp2.RequestHandler):
    def get(self):
        query = Institute.query()
        paramName = getParamName(self.request.url)
        paramValue = self.request.get(paramName)     

        if(param_value):
            query = query.filter(getattr(Institute, paramName) == paraValue)

        data = [institute.to_dict() for institute in query]
        self.response.headers['Content-Type'] = 'application/json; charset=utf-8'
        self.response.write(data2json(data))

    
    def post(self):
        data = json.loads(self.request.body)
        newInstitute = Institute(id=data['cnpj'])
        newInstitute.institute_name = data['institute_name']
        newInstitute.responsible_person_name = data['responsible_person_name']
        newInstitute.cnpj = data['cnpj']
        newInstitute.legal_nature = data['legal_nature']
        newInstitute.address = data['address']
        newInstitute.occupation_area = data['occupation_area']
        newInstitute.description = data['description']
        newInstitute.image_url = data.get('image_url')
        newInstitute.email = data['email']
        newInstitute.phone_number = data['phone_number']
        newInstitute.put()
        self.response.set_status(201)
   
   

class UserHandler(webapp2.RequestHandler):
    def get(self):
        query = User.query()
        data = [user.to_dict() for user in query]
        self.response.headers['Content-Type'] = 'application/json; charset=utf-8'
        self.response.write(data2json(data))

    
    def post(self):
        data = json.loads(self.request.body)
        newUser = User(id = data['cpf'])
        newUser.name = data['name']
        newUser.password = data['password']
        newUser.cpf = data['cpf']
        newUser.photo_url = data.get('photo_url')
        newUser.email = data['email']
        newUser.put()
        self.response.set_status(201)


class PostHandler(webapp2.RequestHandler):
    def get(self):
        query = Post.query()
        data = [post.to_dict() for post in query]
        self.response.headers['Content-Type'] = 'application/json; charset=utf-8'
        self.response.write(data2json(data))
    

    def post(self):
        data = json.loads(self.request.body)
        newPost = Post()
        newPost.institute_name = data['institute_name']
        newPost.author = data['author']
        newPost.likes = data['likes']
        newPost.put()
        self.response.set_status(201)


app = webapp2.WSGIApplication([
    ('/api/institute',InstituteHandler), ('/api/user', UserHandler), ('/api/post', PostHandler) 
], debug=True)





