import csv
from os.path import dirname,join
from classes.alumno import Alumno
from classes.materia import Materia

def loadFileCSV(name):
    list = []
    flag = True
    file = open(join(dirname(__file__),name))
    lista = csv.reader(file,delimiter = ';')
    for row in lista:
        if flag: flag = False
        else: loadRow(list,row,name)
    file.close
    return list

def loadRow(list,row,name):
    if row[0] == '' or row[1] == '' or row[2] == '' or row[3] == '' or row[4] == '' :
        print('Error en la direccion',row)
    else:
        if name == 'alumnos.csv':
            list.append(Alumno(int(row[0]),row[1],row[2],row[3],row[4]))
        else :
            list.append(Materia(int(row[0]),row[1],row[2],int(row[3]),row[4]))
        return list