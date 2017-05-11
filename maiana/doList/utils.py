import json
import webapp2
from google.appengine.ext import ndb
from google.appengine.api import users

def date_handler(obj):
    print ">>>>>>>>>>>>>>>> %s " % obj
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
    
    def authentication(self):    
        user = users.get_current_user()
        if user:
            
            print "esta logado auten"

            nickname = user.nickname()
			logout_url = users.create_logout_url('/')
			self.redirect(logout_url)

        else:

            print "n esta logado auten"
            login_url = users.create_login_url('/')
			self.redirect(login_url)            

    return authentication

    