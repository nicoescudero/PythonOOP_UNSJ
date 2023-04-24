import csv
from os.path import dirname,join
from classes.email import email

def loadFileCSV():
    list = []
    flag = True
    file = open(join(dirname(__file__), 'address.csv'))
    lista = csv.reader(file, delimiter = ';')
    for row in lista:
        if flag == True: flag = False
        else:
            loadRow(list,row)
    file.close()
    return list

def loadRow(list,row):
    address = row[0].split(',')
    if(address[0] == '' or address[1] == ''  or address[2] == ''  or address[3] == ''):
        print('Error en el email: %s', address)
        return
    else:
        print(address)
        return list.append(email(address[0],address[1],address[2],address[3]))