#!/usr/bin/python
# -*- coding: utf-8 -*-

import simplejson
import urllib
import urllib2
import re
import time

url = "https://www.virustotal.com/vtapi/v2/url/report"
key = "YOUR KEY"

f = open('urls2.txt')

line=f.readline()

while line:
	line2 = re.sub('\n','',line)
	parameters = {"resource": line2, "apikey": key}
	data = urllib.urlencode(parameters)
	req = urllib2.Request(url, data)
	try:
		response = urllib2.urlopen(req)
		response1 = response.read()
	except:
		print "Error!"
		break

	decjson = simplejson.loads(response1)
	print "[+] Date :" + decjson["scan_date"]
	print "[+] URL :" + decjson["url"]
	print "[+] Positives :" + str(decjson["positives"]) + " / " + str(decjson["total"])
	print ""

	time.sleep(16)

	line=f.readline()


