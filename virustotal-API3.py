#!/usr/bin/env python
#coding:utf-8

import json
import urllib
import urllib2
import re

url = "https://www.virustotal.com/vtapi/v2/file/report"
parameters = {"resource": "99017f6eebbac24f351415dd410d522d",
                  "apikey": "YOUR KEY"}

data = urllib.urlencode(parameters)
req = urllib2.Request(url, data)
response = urllib2.urlopen(req)
jsondec = json.loads(response.read())

print "[+] Date :" + jsondec["scan_date"]
print "[+] Sample SHA1 :" + jsondec["sha1"]
print "[+] Positives : " + str(jsondec["positives"]) + " / " + str(jsondec["total"])
print ""
