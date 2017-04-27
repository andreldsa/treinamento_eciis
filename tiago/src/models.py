from google.appengine.ext import ndb


class Institution(ndb.Model):

	name = ndb.StringProperty(required=True)
	representativeName = ndb.StringProperty(required=True)
	cnpj = ndb.StringProperty(required=True)
	legal_nature = ndb.StringProperty(required=True)
	address = ndb.StringProperty()
	description = ndb.TextProperty()
	#picture = ndb.BlobProperty() //ver como passar isso por JSON
	email = ndb.StringProperty()
	telephone = ndb.StringProperty()


class User(ndb.Model):

	name = ndb.StringProperty(required=True)
	password = ndb.StringProperty(required=True)
	cpf = ndb.StringProperty(required=True)
	#picture = ndb.BlobProperty() // ver como passar isso por JSON
	email = ndb.StringProperty(required=True)


class Post(ndb.Model):

	institution = ndb.StringProperty(required=True)
	author = ndb.StringProperty(required=True)
	time = ndb.DateTimeProperty(required=True)
	likes = ndb.IntegerProperty()
	