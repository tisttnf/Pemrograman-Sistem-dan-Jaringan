# Deklarasi file
fname = "/proc/cpuinfo"

# Melihat isi file
# cat /proc/cpuinfo

# Membuka file
fd = open(fname)
# fd = open("/proc/cpuinfox") # Error

# Mencoba fungsi fd
dir(fd)
fd.mode
fd.name
fd.closed
fd.read()
fd.read()
fd.tell()
fd.seek(4420)
fd.read()
fd.seek(4020)
fd.read()
fd.seek(0)
fd.read()
fd.seek(0)
fd.readline()
fd.tell()
fd.close()
fd.closed()
# fd.tell() # Error
fd.readlines
fd.seek(0)
data = fd.readlines()
type(data)
data[0]
data[1]
data[2]
len(data)

# Menulis file
# fd.write("Haloo") # Error
fname = "/tmp/file.txt"
fd.close()
fname = "/tmp/file.txt"
fd = open(fname, "w")
strdata = "Halo Dunia\nBaris ke-2\nBaris ke-3"
fd.write(strdata)
fd.close()
fd = open(fname, "w")
strdata = "Ini data baru\nIni baris kedua"
fd.write(strdata)
fd.close()

# Menulis dan membaca file
fd = open(fname, "w+")
strdata = "Ini data baru\nIni baris kedua"
fd.seek(0)
fd.readline()
fd.close(0)

# Menulis diakhir baris
fd = open(fname, "a")
strdata = "Ini data baru tambahan"
strdata = "Ini data baru tambahan\n"
fd.write(strdata)
fd.write(strdata)
fd.close()
fd = open(fname)
fd.readline()
fd.readline()
fd.readline()
fd.readline()

# Menulis diakhir baris dan membaca file
fd = open(fname, "a+")
fd.write("haiiiii\n")