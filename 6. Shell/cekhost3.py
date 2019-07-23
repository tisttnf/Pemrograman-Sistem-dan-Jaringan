import os
# import time

fname = "ip.txt"
fd = open(fname)
# fd mode default yaitu read

fname1 = "status.csv"
fd1 = open(fname1, "a")

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

    cmd1 = "date +'%F %X'"    
    fp1 = os.popen(cmd1)
    outx1 = fp1.read()
    outx1 = outx1.strip()
    
    print("Host %s is %s" %(ipx, status))
    # t = time.strftime("%Y-%m-%d %H:%M:%S")
    # str(t)
    fd1.write("%s;%s;%s\n" %(outx1, ipx, status))    

fd.close()
fd1.close()