import json
from google.appengine.api import users


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

def json2data(jsonStr):
  return json.loads(jsonStr)

def isLoggedIn(func):
  def params(self):
    user = users.get_current_user()
    
    if user:
      return func(self)
    else:     
      greeting = {
        "message" : 'User is offline'
      }
    
      self.response.set_status("401")
      self.response.headers['Content-Type'] = 'application/json; charset=utf-8'
      self.response.write(data2json(greeting))

  return params

def login():
  login_url = users.create_login_url('/')
  return login_url

def logout():
  logout_url = users.create_logout_url('/')
  return logout_url