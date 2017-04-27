from google.appengine.ext import ndb


class Institute(ndb.Model):
    institute_name = ndb.StringProperty(required=True)
    responsible_person_name = ndb.StringProperty(required=True)
    cnpj = ndb.IntegerProperty(required=True)
    legal_nature = ndb.StringProperty(required=True,choices=set(["public", "private", "philanthropic"]))
    address = ndb.StringProperty(required=True)
    occupation_area = ndb.StringProperty(required=True)
    description = ndb.TextProperty(required=True)
    image_url = ndb.TextProperty()
    email = ndb.StringProperty(required=True)
    phone_number = ndb.IntegerProperty(required=True)


class User(ndb.Model):
    name = ndb.StringProperty(required=True)
    password = ndb.StringProperty(required=True)
    cpf = ndb.IntegerProperty(required=True)
    photo_url = ndb.StringProperty()
    email = ndb.StringProperty(required=True)


class Post(ndb.Model):
    institute_name = ndb.StringProperty(required=True)
    author = ndb.StringProperty(required=True)
    publication_date = ndb.DateTimeProperty(auto_now_add=True)
    likes = ndb.IntegerProperty(default=0)