import Utils.Charge as Charge
import Utils.Graphics as gf
import Utils.procesingData as procesingData

def run():
    confirm = False
    while confirm == False:
        FileName = input(f'Ingresar el nombre del archivo ha utilizar o presione enter para salir:')
        if FileName == '':
            data = ''
            break
        else:
            data,confirm = Charge.cargaArchivo(FileName)

    confirm = False
    # menu, cols = procesingData.colNames(data)
    while confirm == False:
        if data == '':
            break
        menu, cols = procesingData.colNames(data)

        use = input(menu)
        if use == "":
            break
        elif use not in cols:
            print('Opcion no valida')
        else:
            var =procesingData.separate(data,use)
            unique,count = procesingData.countValues(var)
            gf.Grafica(unique,count)



if __name__ == "__main__":
    run()




