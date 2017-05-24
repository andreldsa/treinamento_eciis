from google.appengine.ext import ndb


class User(ndb.Model):
    email = ndb.StringProperty()
    lists = ndb.KeyProperty(kind='List', repeated=True)

    def delete_lists(self):
        ndb.delete_multi(self.lists)
        self.put()

    def remove_list(self, list_key):
        self.lists.remove(list_key)
        self.put()

    def add_list(self, list_key):
        self.lists.append(list_key)
        self.put()


class List(ndb.Model):
    title = ndb.StringProperty(required=True)
    description = ndb.TextProperty()
    tasks = ndb.KeyProperty(kind='Task', repeated=True)

    def add_task(self, task_key):
        self.tasks.append(task_key)
        self.put()

    def delete_tasks(self):
        print self.tasks
        ndb.delete_multi(self.tasks)

    def remove_task(self, task_key):
        self.tasks.remove(task_key)
        self.put()

    @staticmethod
    def delete(_list):
        _list.delete_tasks()
        _list.key.delete()

    @staticmethod
    def create(data):
        new_list = List()
        new_list.title = data.get('title')
        new_list.description = data.get('description')
        return new_list.put()


class Task(ndb.Model):
    title = ndb.StringProperty(required=True)
    description = ndb.TextProperty()
    priority = ndb.StringProperty(
        required=True, choices=set(['high', 'medium', 'low']))
    done = ndb.BooleanProperty(default=False)
    list = ndb.KeyProperty(kind='List', required=True)

    def update(self, data):
        for prop in ['title', 'description', 'priority', 'done']:
            setattr(self, prop, data[prop])

        self.put()

    @staticmethod
    def create(data, list_key):
        new_task = Task()
        new_task.title = data.get('title')
        new_task.description = data.get('description')
        new_task.priority = data.get('priority')
        new_task.list = list_key
        return new_task.put()

    @staticmethod
    def delete(task):
        task.key.delete()
