from google.appengine.ext import ndb

class Task(ndb.Model):
    name = ndb.StringProperty(required=True)
    date_created = ndb.DateTimeProperty(auto_now_add=True)
    status = ndb.BooleanProperty(default=False)
    comment = ndb.TextProperty()

class TaskList(ndb.Model):
    name = ndb.StringProperty(required=True)
    tasks = ndb.StringProperty(repeated=True)

class User(ndb.Model):
    name = ndb.StringProperty()
    email = ndb.StringProperty()