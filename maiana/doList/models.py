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
    email = ndb.StringProperty()
    lists = ndb.StringProperty(repeated=True)

    @staticmethod
    def get_by_email(user_email):
        
        user = User.get_or_insert(user_email)
        user.email = user_email
        user.put()
        return user
    
    def add_list(self, list):
        
        self.lists.append(list)
        if(list == "apaga"):
            self.lists = []
        
        print self.lists