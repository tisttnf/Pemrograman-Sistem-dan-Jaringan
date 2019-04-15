def mymax(x) :
    i = 0
    while i < len(x) :        
        try :
            if x[i] > x[i+1] :
                x[i], x[i+1] = x[i+1], x[i]
        except :
            pass        
        i += 1
    return x[i-1]

def mymin(x) :
    i = 0
    while i < len(x) :        
        try :
            if x[i] < x[i+1] :
                x[i], x[i+1] = x[i+1], x[i]
        except :
            pass        
        i += 1
    return x[i-1]