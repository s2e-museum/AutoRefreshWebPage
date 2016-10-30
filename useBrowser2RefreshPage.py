import webbrowser
import time
import os

url = 'http://c.m.163.com/news/l/102331.html?w=2'
for j in range(200):
    webbrowser.open_new(url)
    print('%s %d' % ('count :', j))
