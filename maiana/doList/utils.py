import json
import webapp2
from google.appengine.ext import ndb
from google.appengine.api import users

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
        ensure_ascii=False
    )

def is_logged(method):
    
    def authentication(self, *args):
          
        user = users.get_current_user()
        if user:
            method(self, *args)

        else:   
            self.response.write('{"msg":"requires authentication", "login_url":"http://%s/login"}' % self.request.host)
            self.response.set_status(401)

    return authentication

    