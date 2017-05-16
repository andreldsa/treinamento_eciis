import json
import md5

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
    return func(self, *args)

  return params

def current_user_email():
      return users.get_current_user().email().lower();

def login():
  login_url = users.create_login_url('/')
  return login_url

def logout():
  logout_url = users.create_logout_url('/')
  return logout_url

def gravatar_url(email):
    email_lower = email.lower().strip()
    hash_md5 = md5.md5(email_lower)
    return "http://www.gravatar.com/avatar/%s.jpg" % hash_md5.hexdigest()
