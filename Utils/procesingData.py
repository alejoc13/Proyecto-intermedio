def countValues(var):
    aux = {}
    unique = []
    count = []
    for value in  var:
        if value not in aux.keys():
            aux[value] = 1
        else:
            aux[value] +=1
    for key in aux.keys():
        unique.append(key)
        count.append(aux[key])
    return unique,count

def separate(data,name):
    aux =  list(map(lambda x: x[name],data))
    return aux