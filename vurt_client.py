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
	os.system('pip install -r requirements.txt')
	os.system('cp vurt_client.py /usr/bin')
	os.system('sudo echo -e  >> /etc/crontab "*/5 * * * * /usr/bin/python /usr/bin/vurt_client.py update"')

if(sys.argv[1]=='setup'):
	setup()

if(sys.argv[1]=='update'):
	update()
else:
	print 'usage: setup | update'
