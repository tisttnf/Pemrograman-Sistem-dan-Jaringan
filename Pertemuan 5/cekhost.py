import os

ipx = input("IP Address : ")
pattern = "3 received"

status = "Down"
cmd = "ping -q -c3 %s" %(ipx)
fp = os.popen(cmd)
outx = fp.read()

if outx.find(pattern) > -1 :
    status = "Up"

print("Host %s is %s" %(ipx, status))