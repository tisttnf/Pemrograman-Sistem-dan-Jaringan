fname = "config.cfg"
fd = open(fname, "r")
dataset = fd.readlines()
for row in dataset :
    rec = row.strip()
    cols = rec.split("=")
    k = cols[0]
    v = cols[1]
    print("%s => %s" %(k,v))
fd.close()