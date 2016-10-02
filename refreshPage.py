import urllib.request  
import time  
  
#使用build_opener()是为了让python程序模仿浏览器进行访问  
opener = urllib.request.build_opener()  
opener.addheaders = [('User-agent', 'Mozilla/5.0')]  
  
#refresh a specific page
print('now start to load page：')  
tempUrl = 'http://3g.163.com/ntes/special/00340BF8/seventlive.html?roomid=98246'  
for j in range(50000):  
    try :  
        opener.open(tempUrl)  
        print('%d %s' % (j , tempUrl))  
    except urllib.error.HTTPError:  
        print('urllib.error.HTTPError')  
        time.sleep(1)  
    except urllib.error.URLError:  
        print('urllib.error.URLError')  
        time.sleep(1)  
    #time.sleep(0.1)  