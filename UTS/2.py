fname = "/etc/passwd"
fd = open(fname)

for i in fd.readlines() :    
    user = i.split(":")
    print(user[0])