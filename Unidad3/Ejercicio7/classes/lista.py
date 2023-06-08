from classes.nodo import Nodo
from interfaces.ejercicio5Interface import ClassInterface
from zope.interface import implementer

@implementer(ClassInterface)
class Lista:
    __indice = 0
    __tope = 0
    def __init__(self):
        self.__comienzo = None
        self.__actual = None
    def __iter__(self): return self
    def __next__(self):
        if self.__indice == self.__tope:
            self.__actual = self.__comienzo
            self.__indice = 0
            raise StopIteration
        else:
            self.__indice += 1
            dato = self.__actual.getDato()
            self.__actual = self.__actual.getSiguiente()
            return dato
    #Interface: definicion de agregarElemento 
    def agregarElemento(self,elemento=object):
        nodo = Nodo(elemento)
        nodo.setSiguiente(self.__comienzo)
        self.__comienzo = nodo
        self.__actual = nodo
        self.__tope += 1
    #Interface: definicion de insertarElemento en determinada posicion
    def insertarElemento(self,elemento=object,posicion=0):
        if posicion == 0: self.agregarElemento(elemento)
        else:
            i = 0
            aux = self.__comienzo
            anterior = self.__comienzo
            while i < posicion and aux != None:
                anterior = aux
                aux = aux.getSiguiente()
                i += 1
            if posicion == i:
                nodo = Nodo(elemento)
                anterior.setSiguiente(nodo)
                nodo.setSiguiente(aux)
                self.__tope += 1
            else: raise IndexError('Index not found!')
    #Interface: definicion de mostrarElemento en determinada posicion
    def mostrarElemento(self,posicion=0):
        if posicion == 0: return self.__comienzo.getObjectType()
        else:
            i = 0
            aux = self.__comienzo
            while i < posicion and aux != None:
                aux = aux.getSiguiente()
                i += 1
            if posicion == i:
                return aux.getObjectType()
            else: raise IndexError('Index not found!')
    def buscarDocentesI(self,carrera):
        aux = self.__comienzo
        while aux != None:
            aux.dataDocenteI(carrera)
            aux = aux.getSiguiente()
    def toJSON(self):
        aux = self.__comienzo
        vehiculos = []
        while aux != None:
            vehiculos.append(aux.toJSON())
            aux = aux.getSiguiente()
        dictionary = dict(
            __class__ = self.__class__.__name__,
            Vehiculos = vehiculos
        )
        return dictionary