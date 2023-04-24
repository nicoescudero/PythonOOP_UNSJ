from os.path import dirname, join
import csv

def loadFileTXT():
    list = []
    flag = True
    file = open(join(dirname(__file__),'registroTemperaturas.txt'))
    lista = csv.reader(file,delimiter = ';')
    for row in lista:
        if flag: flag = False
        else: loadRow(list,row)
    file.close
    return list

def loadRow(list,row):
    adrs = row[0].split(',')
    if adrs[0] == '' or adrs[1] == '' or adrs[2] == '' or adrs[3] == '' or adrs[4] == '' :
        print('Error en la direccion',adrs)
    else:
        #list.append(ViajeroFrecuente(int(adrs[0]),int(adrs[1]),adrs[2],adrs[3],int(adrs[4])))
        return list
