#Luiz Fernando da Silva

from google.appengine.ext import ndb

class Task(ndb.Model):

    name_task = ndb.StringProperty(required=True)
    date = ndb.DateTimeProperty(auto_now_add=True)

    @staticmethod
    def createTask(name_task):
        task = Task()
        task.name_task = name_task
        task.put()
        return task

    @staticmethod
    def getAllTasks():
        query = Task.query()
        tasks = [todo.to_dict() for todo in query]
        return tasks

class User(ndb.Model):

    email = ndb.StringProperty(required=True)
    todo_list = ndb.KeyProperty(kind='Task', repeated=True)