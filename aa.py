import urllib, urllib2, cookielib

username = 'oguzhan'
password = 'respect'

cj = cookielib.CookieJar()
opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cj))
login_data = urllib.urlencode({'username' : username, 'password' : password})
opener.open('http://hunt.tyrox.co/get.php', login_data)
resp = opener.open('http://hunt.tyrox.co/get.php')
print resp.read()
