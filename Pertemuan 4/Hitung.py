z = 0
x = 0
y = 0

__author__ = "Budi"
__str__ = "Ini modul perhitungan"

def tambah(x, y) :
    z = x + y
    return z

def kurang(x, y) :
    z = x - y
    return z

def kali(x, y) :
    z = x * y
    return z

def bagi(x, y) :
    try :
        z = x / float(y)
    except :
        z = None
    return z