import csv
def cargaArchivo(FileName):
    data = []
    try:
        with open(FileName,'r') as file:
            reader = csv.reader(file,delimiter=',')
            for row in reader:
                if 'gender' in row:
                    keys = row
                else:
                    aux = {key:val for key,val in  zip(keys,row)}
                    data.append(aux)
        return data,True
    except:
        print("Imposible cargar el archivo")
        return data,False


    


