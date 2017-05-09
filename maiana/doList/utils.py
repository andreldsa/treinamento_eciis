import json
import webapp2
from google.appengine.ext import ndb

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

def loggin(self):
    user = users.get_current_user() #"Pega" o usuário
    if user: # Se está logado
        #Redireciona para o html api
        nickname = user.nickname()
        logout_url = users.create_logout_url('/login')
        greeting = 'Welcome, {}! (<a href="{}">sign out</a>)'.format(
                nickname, logout_url)
    else:
        login_url = users.create_login_url('/api')
        greeting = 
    
    self.response.write()