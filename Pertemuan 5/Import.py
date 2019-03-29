import time
dir(time)
time.localtime()
time.localtime().tm_year
time.localtime().tm_mon
time.strftime('Y')
help(time.strftime)
time.strftime('%Y')
time.strftime('%d-$m-%Y')
tgl = time.strftime('%d-%m-%Y')
print("Tanggal saat ini: %s" %tgl)
import time as t
tgl = t.strftime('%d-%m-%Y')
tgl
from time import strftime
tgl = strftime('%d-%m-%Y')
tgl