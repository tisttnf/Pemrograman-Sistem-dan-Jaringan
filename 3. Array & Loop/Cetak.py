pesan = "Python programming"

def cetak() :
    # Mencetak pesan 5x pertama
    print(pesan)
    print(pesan)
    print(pesan)
    print(pesan)
    print(pesan)
    return 100

def cetak_arg(data,count) :
    for x in range(count) :
        print(data)
    return 200

def cetak_argx(data,count,case="lower") :
    for x in range(count) :
        if case == "upper" :
            print(data.upper())
        else :
            print(data.lower())
    return 300

cetak()
cetak()
st = "Halo Dunia"
c = 10
A = cetak_arg(st, c)
B = cetak_arg("Selamat sore", 5)
C = cetak_argx("Selamat sore", 5, "upper")
print("A is %s" %(str(A)))
print("B is %s" %(str(B)))
print("C is %s" %(str(C)))