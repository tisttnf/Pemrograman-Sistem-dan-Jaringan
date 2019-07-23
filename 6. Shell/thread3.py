"spawn threads until you type 'q'"
import _thread
import time
import os

ips = ["8.8.8.8", "192.168.8.2", "8.8.4.4"]

def cekhost(ip):
    status = "Down"
    pattern = "3 received"
    cmd = "ping -q -c3 %s" %ip
    fp = os.popen(cmd)
    outx = fp.read()
    if outx.find(pattern) > -1 :
        status = "Up"    
    print('Host %s is %s' %(ip,status))

def child(tid):
    time.sleep(3)
    print('Hello from thread', tid)

def parent():    
    for ip in ips :            
        _thread.start_new_thread(cekhost, (ip,))        
        # cekhost(ip)
        time.sleep(2)

parent()