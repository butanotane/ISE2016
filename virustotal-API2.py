#!/usr/bin/env python
#coding:utf-8

import json
import urllib
import urllib2
import re

url = "https://www.virustotal.com/vtapi/v2/file/report"
parameters = {"resource": "99017f6eebbac24f351415dd410d522d",
                  "apikey": "---TOUR API KEY"}

data = urllib.urlencode(parameters)
req = urllib2.Request(url, data)
response = urllib2.urlopen(req)
jsondec = json.loads(response.read())

print (json.dumps(jsondec, sort_keys=True, indent=4, ensure_ascii=False))