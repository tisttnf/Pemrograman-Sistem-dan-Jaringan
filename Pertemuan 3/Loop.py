no = 1
total = 0

while True:
    nil = input("Input nilai ke - %d: " %(no))
    stop = input("Ketik 'q' untuk selesai. ")
    try:
        total = total + float(nil)

        if stop.lower() == "q":
            break

        no += 1
    except:
        print("Nilai harus bilangan" )

rata = total / no
print("Total : %0.2f, rata-rata : %0.2f" %(total,rata))
