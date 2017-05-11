from google.appengine.ext import ndb



class User(ndb.Model):
    name = ndb.StringProperty(required=True)
    email = ndb.StringProperty(required=True)
    lists = ndb.KeyProperty(kind='List', repeated=True)


class List(ndb.Model):
    title = ndb.StringProperty(required=True)
    description = ndb.TextProperty()
    tasks = ndb.KeyProperty(kind='Task', repeated=True)


class Task(ndb.Model):
    title = ndb.StringProperty(required=True)
    description = ndb.TextProperty()
    priority = ndb.StringProperty(required=True, choices=set(['high','medium','low']))
    done = ndb.BooleanProperty(default=False)
    list = ndb.KeyProperty(kind='List', required=True)
    