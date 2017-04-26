from google.appengine.ext import ndb

class Counter(ndb.Model):
    updates = ndb.IntegerProperty(default=0)
    minutes = ndb.IntegerProperty(default=0)


class ToDo(ndb.Model):
    title = ndb.StringProperty(required=True)
    author = ndb.StringProperty()
    text = ndb.TextProperty()
    deadline = ndb.DateTimeProperty()
    keyword = ndb.StringProperty(repeated=True)
    updates = ndb.IntegerProperty(default=0)
