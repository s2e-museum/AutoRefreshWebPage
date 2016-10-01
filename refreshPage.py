import urllib
import urllib.request
import time
print('now start to try to load page')

i=0
while( i < 100):
	time.sleep(1)
	print(i)
	urllib.request.urlopen('http://c.m.163.com/news/l/99092.html?w=7')
	i += 1
