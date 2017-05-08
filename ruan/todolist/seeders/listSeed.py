#!/usr/bin/env python
# coding: utf-8

import json
import requests

BASE = "http://localhost:8080/api/"

ENTITY = "list"

data = [
    {
        'title': 'List 01',
        'description': 'An interisting list'
    },
    {
        'title': 'List 02',
        'description': 'An list to pay attention'
    },
    {
        'title': 'List 03',
        'description': 'Things to do tomorrow'
    },
]

for d in data:
    post = requests.post(BASE + ENTITY,
                         data=json.dumps(d))
    print post.text
