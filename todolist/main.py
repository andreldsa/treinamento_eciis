import webapp2
import json
import datetime
import logging

from models import *
from utils import *
def _assert(condition, status_code, msg):
    if condition:
        return

    # TODO: logging here
    webapp2.abort(status_code, msg)

class MinhaException(Exception): pass
class MinhaOutraException(Exception): pass
class MaisUmaException(Exception): pass


class BaseHandler(webapp2.RequestHandler):
    def handle_exception(self, exception, debug):
        logging.error("bla bla")
        self.response.write("oops! deu ruim: " + str(exception))



class ToDosHandler(BaseHandler):
    def get(self):
            query = ToDo.query()
            todos = [todo.to_dict() for todo in query]
            self.response.headers['Content-Type'] = 'application/json; charset=utf-8'
            counter = Counter.get_or_insert("total")
            raise MinhaException("aqui eu forcei a barra")
            data = {
                'total_updates': counter.updates,
                'minutes': counter.minutes,
                'todos': todos
            }
            self.response.write(data2json(data))
                

    def post(self):
        data = json.loads(self.request.body)
        newtodo = ToDo()
        newtodo.title = data['title']
        newtodo.author = data.get('author')
        newtodo.text = data.get('text')
        deadline = data.get('deadline', datetime.datetime.now().isoformat().split(".")[0])
        newtodo.deadline = datetime.datetime.strptime(deadline, "%Y-%m-%dT%H:%M:%S")
        newtodo.put()
        self.response.write('{"iid": "%d"}' % newtodo.key.integer_id())
        self.response.set_status(201)


class UpdateHandler(BaseHandler):
    def get(self):
        counter = Counter.get_or_insert('total')
        counter.minutes += 1
        counter.put()


class ToDoHandler(BaseHandler):


    def put(self, iid):
        @ndb.transactional(retries=0, xg=True)
        def updateToDo(todo, data):
            todo.title = data.get('title', todo.title)
            todo.author = data.get('author', todo.author)
            todo.text = data.get('text', todo.author)
            todo.updates = (todo.updates or 0) + 1
            todo.put()
            counter = Counter.get_or_insert("total")
            counter.updates += 1
            counter.put()

            
        data = json.loads(self.request.body)
        todo = ToDo.get_by_id(int(iid))
        _assert(todo, 400, '{"msg": "invalid integer id"}')
        updateToDo(todo, data)
        self.response.set_status(200)

app = webapp2.WSGIApplication([
    ('/api/todo', ToDosHandler),
    ('/api/update', UpdateHandler),
    ('/api/todo/(.*)', ToDoHandler),
], debug=True)

def erro404(request, response, exception):
    response.write("url invalida: " + str(exception))

app.error_handlers[404] = erro404
