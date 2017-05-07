import webapp2
import sys
import json

sys.path.append("model")

from tarefas import Tarefa

def date_handler(obj):
  if hasattr(obj, 'isoformat'):
    return obj.isoformat()
  elif hasattr(obj, 'email'):
    return obj.email()

  return obj

def data2json(data):
  return json.dumps(
    data,
    default=date_handler,
    indent=2,
    separators=(',', ': '),
    ensure_ascii=False)

class MainHandler(webapp2.RequestHandler):

    def get(self):

        query = Tarefa.query()
        data = [todo.to_dict() for todo in query]

        self.response.headers['Content-Type'] = 'application/json; charset=utf-8'
        self.response.write(data2json(data))

    def post(self):

        data = json.loads(self.request.body)

        tarefa = Tarefa()
        tarefa.nome_tarefa = data['nome_tarefa']
        tarefa.put()
        self.response.set_status("201")
        self.response.write(tarefa.key.integer_id())
        self.response.write("\n")



app = webapp2.WSGIApplication([
    ("/api/todo", MainHandler),
], debug=True)
