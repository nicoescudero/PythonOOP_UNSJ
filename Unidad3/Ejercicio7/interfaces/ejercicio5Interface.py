from zope.interface import Interface

class ClassInterface(Interface):
    #a- Insertar un objeto en una posicion determinada
    def insertarElemento(elemeto=object,posicion=0): pass
    #b- Agregar un elemento al final de una colección
    def agregarElemento(elemento=object):pass
    #c- Mostrar un elemento dada una posición de la colección
    def mostrarElemento(posicion=0): pass