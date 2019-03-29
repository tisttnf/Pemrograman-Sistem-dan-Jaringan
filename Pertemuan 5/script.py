# Ubah kode berikut kedalam bentuk tulisan dengan nama config.cfg

# database = mysql
# user = root
# password = rahasia
# dbname = dbpegawai
# host = localhost

fname = "config.cfg"
fd = open(fname, "w+")
strdata = "database = mysql\nuser = root\npassword = rahasia\ndbname = dbpegawai\nhost = localhost\n"
fd.write(strdata)
fd.close()

# cat config.cfg

fd = open(fname, "a")
fd.write("database = mysql\n")
fd.write("user = root\n")
fd.write("password = rahasia\n")
fd.write("dbname = dbpegawai\n")
fd.write("host = localhost\n")
fd.close()

x = "database = mysql\n"
y = x.strip()
z = y.split("=")
print("%s => %s" %(z[0],z[1]))
# print(f"{z[0]} => {z[1]}")

fd = open(fname, "r")
dataset = fd.readlines()
for row in dataset :
    rec = row.strip()
    cols = rec.split("=")
    k = cols[0]
    v = cols[1]
    print("%s => %s" %(k,v))
fd.close()