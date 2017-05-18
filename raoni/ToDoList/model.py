from google.appengine.ext import ndb
import datetime

class Task(ndb.Model):
    name = ndb.StringProperty(required=True)
    deadline = ndb.DateProperty()
    description = ndb.StringProperty(required=True)

    @staticmethod
    def createTask(data):
        task = Task()
        task.name = data['name']
        task.description = data['description']
        deadline = data.get('deadline').split('/')
        task.deadline = datetime.date(int(deadline[0]), int(deadline[1]), int(deadline[2]))
        task_key = task.put()
        return task_key


class User(ndb.Model):
    tasks = ndb.KeyProperty(kind='Task', repeated=True)
    email = ndb.StringProperty(required=True)

    @staticmethod
    def createTask(user_google, data):
        task_key = Task.createTask(data)
        user_email = user_google.email().lower()
        user = User.get_or_insert(user_email, email=user_email)
        user.tasks.append(task_key)
        user.put()

    @staticmethod
    def loadTask(user_google):
        user_email = user_google.email().lower()
        user = User.get_or_insert(user_email, email=user_email)
        user_tasks = []
        for task in user.tasks:
            task_id = task.id()
            task_append = task.get().to_dict()
            task_append['id'] = task_id
            user_tasks.append(task_append)
        return user_tasks

    @staticmethod
    def deleteTask(user_google, id):
        user_email = user_google.email().lower()
        user = User.get_by_id(user_email)
        finded = False
        for i in xrange(len(user.tasks)):
            if user.tasks[i].id() == int(id):
                task = user.tasks[i]
                task.delete()
                user.tasks.pop(i)
                user.put()
                finded = True
                break
        return finded