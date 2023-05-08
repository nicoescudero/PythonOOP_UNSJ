from os.path import dirname, join
from classes.registro import Registro
def loadFileTXT():
    list = [[ 0 for colum in range(24)]for fila in range(2)]
    flag = True
    file = open(join(dirname(__file__),'register.txt'),'r')
    lista = file.readlines()
    for row in lista:
        if flag: flag = False
        else: loadRow(list,row)
    file.close
    return list

def loadRow(list,row):
    row = row.split(',')
    if row[0] == '' or row[1] == '' or row[2] == '' or row[3] == '' or row[4] == '' :
        print('Error en la direccion',row)
    else:
        day = int(row[0]) - 1
        time = int(row[1]) - 1
        register = Registro(int(row[2]),int(row[3]),int(row[4]))
        list[day][time] = register
        return list