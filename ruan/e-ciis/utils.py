import json
import datetime


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


def getParamName(url):
    param_name = ''
    if('?' in url):
        param_name = url.split('?')[1].split('=')[0]

    return param_name