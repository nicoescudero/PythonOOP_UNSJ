import json
from os.path import dirname,join
from classes.lista import Lista
from classes.vNuevo import VehiculoNuevo
from classes.vUsado import VehiculoUsado

class ObjectEncoder(object):
    #Decodificar diccionariot()
    def decodeDictionary(self,d):
        if '__class__' not in d:
            return d
        else:
            class_ = eval(d['__class__'])#Guarda el nombre de la clase 
            if d['__class__'] == 'Lista':
                vehiculosList = d['Vehiculos']#guarda la segunda propiedad del archivo JSON, que es vehiculos
                lista = class_()#Instancia la clase Lista
                for i in range(len(vehiculosList)):#Recorre todos los vehiculos del archivo
                    vehiculoItem = vehiculosList[i]#es la informacion de cada item de los vehiculos
                    class_name = vehiculoItem.pop('__class__')#Extrae su clase
                    class_ = eval(class_name)#Guarda la clase vehiculo
                    atributos = vehiculoItem.pop('__atributos__')#Guarda los atributos que tiene
                    vehiculo = class_(**atributos)#Creacion del objeto vehiculo segun su clase: usado o nuevo
                    lista.agregarElemento(vehiculo)#Agrega el objeto en la lista
                return lista
    #Guardar JSON
    def saveJSON(self,dictionary,file):
        pathFile = join(dirname(__file__),file)
        with open(pathFile, 'w',encoding='UTF-8') as address:
            json.dump(dictionary,address,indent=4)
            address.close()
    #Leer JSON
    def readJSON(self,file):
        pathFile = join(dirname(__file__),file)
        with open(pathFile,'r', encoding='utf-8') as fuente:
            dictionary = json.load(fuente)
            fuente.close()
            return dictionary
    #Convertir texto a diccionario
    def convertTextToDictionary(self,text):
        return json.loads(text)