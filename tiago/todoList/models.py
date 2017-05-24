# -*- coding: utf-8 -*-
"""Models."""

from google.appengine.ext import ndb
from google.appengine.api import mail
import datetime


class User(ndb.Model):
    """Class User."""

    keys_tasks = ndb.IntegerProperty(repeated=True)

    def update(self, data):
        """Update the tasks of user."""
        update = {}
        if data.get('operation') == 'add':
            task = self.add_task(data)
            update = {
                'name': task.name,
                'description': task.description,
                'deadline': task.deadline,
                'id': task.key.id()
            }

        else:
            self.del_task(data)

        self.put()
        return update

    def add_task(self, data):
        """Add a task."""
        task = Task()
        task.name = data.get('name')
        task.description = data.get('description')
        task.deadline = data.get('deadline')
        key = task.put()
        self.keys_tasks.append(key.id())
        return task

    def del_task(self, data):
        """Delete a task."""
        taskID = data.get('id')
        self.keys_tasks.remove(taskID)
        ndb.Key(Task, taskID).delete()

    def get_tasks(self):
        """Return all the tasks of user."""
        tasks = []

        if len(self.keys_tasks) > 0:
            for taskID in self.keys_tasks:
                task = Task.get_by_id(taskID)
                tasks.append({
                    'name': task.name,
                    'description': task.description,
                    'deadline': task.deadline,
                    'id': taskID
                })

        return tasks

    def get_data(self):
        """Change the data of user to dictionary."""
        data = {
            "email": self.key.id(),
            "user": self.to_dict(),
            "tasks": self.get_tasks()
        }

        return data

    def send_email(self):
        """Send email for user."""
        expiring_tasks = []
        for taskID in self.keys_tasks:
            task = Task.get_by_id(taskID)
            if task.expiring:
                expiring_tasks.append('Sem nome' if len(
                    task.name) == 0 else task.name)

        if len(expiring_tasks) > 0:
            num_tasks = str(len(expiring_tasks))
            tasks = ', '.join(expiring_tasks)
            message = 'A(s) seguinte(s) tarefa(s) esta(ao) \
            expirando: %s' % tasks
            mail.send_mail(
                sender='tiago.pereira@ccc.ufcg.edu.br',
                to=self.key.id(),
                subject='Voce tem ' + num_tasks +
                ' tarefa(s) proxima(s) de expirar',
                body=message
            )


class Task(ndb.Model):
    """Class Task."""

    name = ndb.StringProperty()
    description = ndb.StringProperty()
    deadline = ndb.StringProperty()
    expiring = ndb.BooleanProperty()

    def verify_deadline(self):
        """Verify the deadline of task."""
        current_time = datetime.datetime.now().date()
        if self.prazo:
            data = self.deadline.split('T')[0].split('-')
            deadline = datetime.datetime(
                int(data[0]), int(data[1]), int(data[2]))
            time_left = deadline.date() - current_time
            self.expiring = time_left <= datetime.timedelta(
                2) and time_left >= datetime.timedelta(0)
        else:
            self.expiring = False

        self.put()
