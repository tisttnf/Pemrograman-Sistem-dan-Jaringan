import os

fname = "ip.txt"
fd = open(fname)

pattern = "3 received"

for ip in fd.readlines() :    
    status = "Down"
    outx = None
    # strip untuk menghilangkan karakter \n
    ipx = ip.strip()

    cmd = "ping -q -c3 %s" %(ipx)
    fp = os.popen(cmd)
    outx = fp.read()

    if outx.find(pattern) > -1 :
        status = "Up"

    print("Host %s is %s" %(ipx, status))    