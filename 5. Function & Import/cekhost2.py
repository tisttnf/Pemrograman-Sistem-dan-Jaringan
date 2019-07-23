import os

fname = "ip.txt"
fd = open(fname, "r")
data = fd.readlines()
j = 0
for i in data :
    data[j] = i.strip()
    pattern = "3 received"

    status = "Down"
    cmd = "ping -q -c3 %s" %(data[j])
    fp = os.popen(cmd)
    outx = fp.read()

    if outx.find(pattern) > -1 :
        status = "Up"

    print("Host %s is %s" %(data[j], status))
    j += 1