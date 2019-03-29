while True :
    kata = input("Ketikkan text (q untuk Exit) : ")
    baru = ""    

    if kata.lower() == "q" :
        break

    i = 0
    k = len(kata) - 1
    while i < len(kata) :
        baru += kata[k]
        i += 1
        k -= 1

    print(baru)    