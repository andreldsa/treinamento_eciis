from google.appengine.ext import ndb


class Institution(ndb.Model):
	name = ndb.StringProperty(required = True)
	reponsable_name = ndb.StringProperty(required=True)
	cnpj = ndb.StringProperty(required=True)
	nature = ndb.StringProperty(required=True, choices = set(['Publico', 'Privado', 'Filantropico']))
	adress = ndb.StringProperty(required=True)
	field_of_work = ndb.StringProperty(required = True)
	description = ndb.StringProperty(required=True)
	email = ndb.StringProperty(required=True)
	phone = ndb.StringProperty(required=True)



class User(ndb.Model):
	name = ndb.StringProperty(required=True)
	password = ndb.StringProperty(required=True)
	cpf = ndb.StringProperty(required=True)
	email = ndb.StringProperty(required=True)





class Post(ndb.Model):
	institution_name = ndb.StringProperty(required=True)
	author_name = ndb.StringProperty(required=True)
	date = ndb.DateTimeProperty(required=True)
	likes = ndb.IntegerProperty(required=True)

