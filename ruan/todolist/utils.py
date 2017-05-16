from google.appengine.ext import ndb

import json
import datetime

from google.appengine.api import users
from models import User


def date_handler(obj):
  if hasattr(obj, 'isoformat'):
    return obj.isoformat()
  elif hasattr(obj, 'email'):
    return obj.email()
  
  if isinstance(obj, ndb.Key):
      return obj.integer_id()

  return obj


def data2json(data):
  return json.dumps(
    data,
    default=date_handler,
    indent=2,
    separators=(',', ': '),
    ensure_ascii=False)


def data2dict(data):
    newDict = data.to_dict()
    newDict['id'] = data.key.id()
    return newDict


def login_required(method):
    def check_login(self, *args):
        google_user = users.get_current_user()

        if google_user is None:
            self.response.write('{"msg":"requires authentication", "login_url":"http://%s/login"}' %self.request.host)
            self.response.set_status(401)
            return
        
        user = User.get_or_insert(google_user.email().lower())
        method(self, user, *args)
    
    return check_login