import json
import webapp2
from models import *
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


def dict_json(data):

    print data

    out = data.to_dict()
    out['id'] = data.key.id()
    return out


def get_list(data):

        print data
        output = []
        lists = data['lists']
        for key in lists:
            list = List.get_by_id(key.id())


            if(list is None):
                pass
            else:
                output.append(list.name)

        data['lists_name'] = output
        return data


def is_logged(method):

    def authentication(self, *args):
        user = users.get_current_user()
        if user:
            user_email = user.email().lower()
            method(self, user_email, *args)
        else:
            self.response.write(
                '{"msg":"requires authentication", "login_url":"http://%s/login"}' 
                % self.request.host)
            self.response.set_status(401)

    return authentication
