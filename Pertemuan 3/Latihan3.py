no = 1
total = 0.0
e = []
while True:
    nil = input(f'input nilai ke {no} = ')
    try:
        e.append(float(nil))
        stop = input('ketik q untuk selesai = ')

        if(stop.lower() == 'q'):
            total = total + sum(e)
            rata = total / no
            print(f'total nilai : {total:0.2} rata rata nilai : {rata:0.2}')
            break

        else:
            no=no+1
            continue
    except:
        print('nilai yang harus anda masukan bilangan')