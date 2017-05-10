#!/usr/bin/env python
# coding: utf-8

import json
import requests

BASE = "http://localhost:8080/api/"

ENTITY = "list/{0}/task"

# set the ids according to the lists ids created in the listsSeed
lists_ids = ['5066549580791808',
                '5629499534213120',
                    '6192449487634432'];


data = [
    {
        'title': 'Task A',
        'description': 'Very importat task A',
        'priority': 'high'
    },
    {
        'title': 'Task B',
        'description': 'Important task B',
        'priority': 'medium'        
    },
    {
        'title': 'Task C',
        'description': 'Not so much important task C',
        'priority': 'low'       
    },
]

for id in lists_ids:
    for d in data:
        post = requests.post(BASE + ENTITY.format(id),
                            data=json.dumps(d))
        print post.text

