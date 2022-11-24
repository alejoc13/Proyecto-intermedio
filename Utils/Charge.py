import csv
def cargaArchivo(FileName):
    try:
        data = []
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
        return False


    


