import json
import logging
from google.appengine.api import users

class AuthorizationExeption(Exception):
      def __init__(self, msg=None):
            super(AuthorizationExeption, self).__init__(msg or 'User is offline')

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

def _assert(condition):
    if condition:
        return
    raise AuthorizationExeption()

def login_required(func):
  def params(self, *args):
    user = users.get_current_user()
    
    _assert(user != None)
    return func(self, user, *args)

  return params

def login():
  login_url = users.create_login_url('/')
  return login_url

def logout():
  logout_url = users.create_logout_url('/login')
  return logout_url