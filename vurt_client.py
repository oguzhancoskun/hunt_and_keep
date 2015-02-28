#!/usr/bin/python

import urllib,urllib2,sys,os

def update():
	url = 'http://hunt.tyrox.co/get.php'
	data = {'username':'oguzhan','password':'respect'}
	data = urllib.urlencode(data)
	request = urllib2.Request(url + '?' + data)
	response = urllib2.urlopen(request)

def setup():
	os.system('wget https://bootstrap.pypa.io/get-pip.py')
	os.system('python get-pip.py')

if(sys.argv[1]=='setup'):
	setup()
