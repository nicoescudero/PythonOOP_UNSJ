import json
from os.path import dirname,join
from classes.lista import Lista
from classes.docente import Docente
from classes.docenteInvestigador import DocenteInvestigador
from classes.investigador import Investigador
from classes.personalApoyo import PersonalApoyo

class ObjectEncoder(object):
    #Decodificar diccionario()
    def decodeDictionary(self,d):
        if '__class__' not in d:
            return d
        else:
            class_ = eval(d['__class__']) 
            if d['__class__'] == 'Lista':
                personalList = d['Personal']
                lista = class_()#Instancia la clase Lista
                for i in range(len(personalList)):
                    personalItem = personalList[i]#es la informacion de cada item del archivo
                    class_name = personalItem.pop('__class__')#Extrae su clase
                    class_ = eval(class_name)#Tipo de Clase
                    atributos = personalItem.pop('__atributos__')#Guarda los atributos que tiene
                    personal = class_(**atributos)#Creacion del objeto segun su clase
                    lista.agregarElemento(personal)#Agrega el objeto en la lista
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