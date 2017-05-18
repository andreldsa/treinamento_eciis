# Luiz Fernando da Silva
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
        return task
    
    @staticmethod
    def format_task(task):
        task_dict = task.to_dict()
        task_dict['id'] = task.key.integer_id()
        return task_dict

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
    def add_task(name_task, user_email):
        task = Task.createTask(name_task)
        userData = User.get_by_email(user_email)
        task_dict = Task.format_task(task)

        userData.tasks.append(task.key)
        userData.put()
        return task_dict


    @staticmethod
    def get_or_insert_by_email(email):
        user = User.get_or_insert(email)
        user.email = email
        user.gravatar_url = gravatar_url(email)
        user.put()
        return user

    @staticmethod
    def get_by_email(email):
        user = User.get_by_id(email)
        return user

    def get_tasks(self):
        tasks = []
        for task_key in self.tasks:
            task_dict = Task.format_task(task_key.get())
            tasks.append(task_dict)
        return tasks

    @staticmethod
    def make_user(email):
        user = User.get_or_insert_by_email(email)

        user_data = {
            "email": user.email,
            "gravatar_url": user.gravatar_url
        }

        return user_data

    @staticmethod
    @ndb.transactional(retries=0, xg=True)
    def del_task(task_id, user_id):
        task_key = ndb.Key('Task', task_id)
        user = User.get_by_id(user_id)
        task_dict = Task.format_task(task_key.get())

        task_key.delete()
        user.tasks.remove(task_key)
        user.put()
        return task_dict
