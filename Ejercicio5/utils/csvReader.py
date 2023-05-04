import csv
from os.path import dirname,join
from classes.planAhorro import PlanAhorro

def loadFileCSV():
    list = []
    flag = True
    file = open(join(dirname(__file__),'planes.csv'))
    lista = csv.reader(file,delimiter = ';')
    for row in lista:
        if flag: flag = False
        else: loadRow(list,row)
    file.close
    return list

def loadRow(list,row):
    if row[0] == '' or row[1] == '' or row[2] == '' or row[3] == '' or row[4] == '' or row[5] == '':
        print('Error en la direccion',row)
    else:
        list.append(PlanAhorro(int(row[0]),row[1],row[2],int(row[3]),int(row[4]),int(row[5])))
        return