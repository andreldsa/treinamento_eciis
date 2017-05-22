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
    def loadTasks(user_google):
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

    @staticmethod
    def loadTask(user_google, id):
        user_email = user_google.email().lower()
        user = User.get_or_insert(user_email, email=user_email)
        for task in user.tasks:
            if task.id() == int(id):
                task_to_return = task.get().to_dict()
                task_to_return['id'] = int(id)
                return task_to_return
        return None

    @staticmethod
    def editTask(user_google, id, data):
        user = User.get_by_id(user_google.email().lower())
        task_to_edit = None
        for task in user.tasks:
            if task.id() == int(id):
                task_to_edit = task.get()
        if task_to_edit:
            field = data['field']
            value = data['value']
            User.setField(task_to_edit, field, value).put()
            user.put()
            return True
        else:
            return False

    @staticmethod
    def setField(task, field, value):
        if field == 'name':
            task.name = value
        elif field == 'deadline':
            deadline = value.split('/')
            task.deadline = datetime.date(int(deadline[0]), int(deadline[1]), int(deadline[2]))
        elif field == 'description':
            task.description = value
        return task