from google.appengine.ext import ndb


class Task(ndb.Model):
    name = ndb.StringProperty(required=True)
    date_created = ndb.DateTimeProperty(auto_now_add=True)
    status = ndb.BooleanProperty(default=False)
    comment = ndb.TextProperty()


class List(ndb.Model):
    name = ndb.StringProperty(required=True)
    tasks = ndb.KeyProperty(kind=Task, repeated=True)

    def add_task(self, task):
        self.tasks.append(task)

    def remove_task(self, task):
        self.tasks.remove(task)


class User(ndb.Model):
    email = ndb.StringProperty()
    lists = ndb.KeyProperty(kind=List, repeated=True)

    @staticmethod
    def insert(user_email):
        user = User(id=user_email)
        user.email = user_email
        user.put()
        return user

    def add_list(self, list):
        self.lists.append(list)

    def remove_list(self, list):
        self.lists.remove(list)
