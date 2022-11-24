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

def colNames(data):
    menu = ''
    cols = [names for names in data[0].keys()]
    for i in range (len(cols)):
        menu = menu+  str(i)+". "+ str(cols[i])+"\n"
    menu = menu + "Eleja una de las opciones disponibles escribiendo el nombre de la columna para ver el conteo de sus datos: "
    return menu

