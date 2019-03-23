# pesan = "my name is Ardith"
#
# def cetak():
#     print(pesan)
#     print(pesan)
#     print(pesan)
#     print(pesan)
#     print(pesan)
#
# cetak()
# cetak()
# cetak()


# def cetak_arg(data,count):
#     for x in  range(count):
#         print(data)
#
# str = "Halo Dunia"
# c = 100
# cetak_arg(str,c)
# cetak_arg("selamat sore",1)


def cetak_argx (data,count,case="lower"):
    for x in range(count):
        if case == "upper":
            print(data.upper())
        else:
            print(data.lower())
    return 300

A = cetak_argx("Selamat sore",3)
B = cetak_argx("Selamat Siang Ardith!",5,"upper")

#mengembalikan nilai 300
print("A is %s" %(str(A)))
print("B is %s" %(str(B)))