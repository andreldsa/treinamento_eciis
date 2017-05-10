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
        user = users.get_current_user() #"Pega" o usuario

        if user: # Se esta logado
            #Redireciona para o html api
            nickname = user.nickname()
            logout_url = users.create_logout_url('/login')
            #continua a execucao
            self.response.set_status(202) # Accept
            method()
        else:
            
            login_url = users.create_login_url('/api') #Abrir a pag de loggin google e redireciona pra api
            #greeting = {
            #    "login_url" : login_url
            #}
            self.response.set_status(401) # Nao autorizado
            #self.response.headers['Content-Type'] = 'application/json; charset=utf-8'
            #self.response.write(data2json(greeting))

            
        
    
    return authentication
   