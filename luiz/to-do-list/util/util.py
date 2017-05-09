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
      nickname = user.nickname()
      logout_url = users.create_logout_url('/')
      greeting = 'Welcome, {}! (<a href = "{}">sign out</a>)'.format(nickname, logout_url)
        
    else:     
      login_url = users.create_login_url('/')
      greeting = {
        "login_url" : login_url
      }
    
      self.response.set_status("401")
      self.response.headers['Content-Type'] = 'application/json; charset=utf-8'
      self.response.write(data2json(greeting))

    if user:
      return func(self)
    
  return params