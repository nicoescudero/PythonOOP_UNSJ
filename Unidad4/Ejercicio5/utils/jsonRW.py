import json
from os.path import dirname,join
from model.pelicula import Pelicula

class ObjectEncoder(object):
    #Decodificar diccionariot()
    def decodeDictionary(self,d):
        lista = []
        results = d['results']
        for i in range(len(results)):
            titulo = results[i].pop('title')
            resumen = results[i].pop('overview')
            lenguajeOriginal = results[i].pop('original_language')
            fechaEstreno = results[i].pop('release_date')
            genero = results[i].pop('genre_ids')[0]
            pelicula = Pelicula(titulo,resumen,lenguajeOriginal,fechaEstreno,genero)
            lista.append(pelicula)
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