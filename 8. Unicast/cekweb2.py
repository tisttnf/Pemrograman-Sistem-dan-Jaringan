import requests
import threading

class myThread (threading.Thread):
    def __init__(self,url):
        threading.Thread.__init__(self)
        self.url = url

    def run(self):        
        try :                    
            con = requests.get(url)
            print("web server of %s is Running" %(url))
        except :
            print("web server of %s is Stopped" %(url))

fname = "web.txt"
fd = open(fname)

for url in fd.readlines() :
    url = url.strip()    
    thread = myThread(url)
    thread.start()    