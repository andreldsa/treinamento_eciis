from google.appengine.ext import ndb

import json
import datetime


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