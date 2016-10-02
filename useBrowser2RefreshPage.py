import webbrowser  
import time  
import os  
  
url = 'http://3g.163.com/ntes/special/00340BF8/seventlive.html?roomid=98246'
for j in range(100):  
	webbrowser.open_new(url)
	print('%s %d' % ('count :' , j))
	
