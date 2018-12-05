#!/usr/bin/env python3

import sys,os
import urllib.request
import json

url = 'https://qiita.com/api/v2/authenticated_user/items'
req = urllib.request.Request(url)
req.add_header('Authorization', os.getenv('AUTHORIZATION'))
with urllib.request.urlopen(req) as res:
    items = json.load(res)

for item in items:
    print(item['title'])
