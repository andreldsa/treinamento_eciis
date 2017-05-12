from google.appengine.ext import ndb


class Task(ndb.Model):
    name = ndb.StringProperty(required=True)
    deadline = ndb.DateProperty()
    description = ndb.StringProperty(required=True)


class User(ndb.Model):
    tasks = ndb.KeyProperty(kind='Task', repeated=True)
    email = ndb.StringProperty(required=True)



