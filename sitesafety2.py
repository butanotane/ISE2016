# -*- coding: utf-8 -*-
import mechanize
from BeautifulSoup import BeautifulSoup
import time
import re

browser = mechanize.Browser()
browser.set_handle_robots(False)

url = 'http://global.sitesafety.trendmicro.com/'

f = open('urls.txt')

line=f.readline()

while line:
		line2 = re.sub('\n','',line)
		page = browser.open(url)
		browser.select_form(name="urlForm")
		browser.form['urlname']=line2
		browser.submit()

		response=browser.response()
		soup =BeautifulSoup(response.read())
		result=soup.find('div',attrs={'class':'labeltitleresult'})

		print line2 + " :  " + result.string
		time.sleep(5)

		line=f.readline()
