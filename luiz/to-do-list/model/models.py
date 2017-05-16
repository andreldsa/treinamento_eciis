#Luiz Fernando da Silva
from google.appengine.ext import ndb
from util import gravatar_url

class Task(ndb.Model):
    name_task = ndb.StringProperty(required=True)
    date = ndb.DateTimeProperty(auto_now_add=True)

    @staticmethod
    def createTask(name_task):
        task = Task()
        task.name_task = name_task
        task.put()
        return task.key

    @staticmethod
    def getAllTasks():
        query = Task.query()
        tasks = [todo.to_dict() for todo in query]
        return tasks

class User(ndb.Model):
    email = ndb.StringProperty()
    tasks = ndb.KeyProperty(kind='Task', repeated=True)
    gravatar_url = ndb.StringProperty()

    @staticmethod
    def get_or_insert_by_email(email):
        user = User.get_or_insert(email)
        user.gravatar_url = gravatar_url(email)
        user.put()
        return user

    @staticmethod
    def get_by_email(email):
        user = ndb.Key('User','luiz.silva@ccc.ufcg.edu.br').get()
        return user

    def get_tasks(self):
        return [task_key.get().to_dict() for task_key in self.tasks]