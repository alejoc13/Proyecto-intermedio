import Utils.Charge as Charge
import Utils.Graphics as gf
import Utils.procesingData as procesingData
confirm = False
while confirm == False:
    FileName = input(f'Ingresar el nombre del archivo ha utilizar o presione enter para salir:')
    if FileName == '':
        break
    else:
        data,confirm = Charge.cargaArchivo(FileName)

use = input(procesingData.colNames(data))
var =procesingData.separate(data,use)
unique,count = procesingData.countValues(var)
gf.Grafica(unique,count)








