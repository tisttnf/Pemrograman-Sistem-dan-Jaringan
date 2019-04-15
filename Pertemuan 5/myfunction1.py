def mymax(data) :
    z = data[0]
    for x in data :
        if x >= z :
            z = x
    return z

def mymin(data) :
    z = data[0]
    for x in data :
        if x <= z :
            z = x
    return z