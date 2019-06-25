list = ['xyx','hai','abc','xyz','aba','2002']
list2 = []

for i in list :
    if len(i) >= 2 :
        if i[0] == i[len(i)-1] :
            list2.append(i)
print(list2)