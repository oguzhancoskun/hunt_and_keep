#!/usr/bin/python

import urllib,urllib2

url = 'http://hunt.tyrox.co/get.php'
data = {'username':'oguzhan','password':'respect'}
data = urllib.urlencode(data)
request = urllib2.Request(url + '?' + data)
response = urllib2.urlopen(request)

