class Vehiculo:
    def __init__(self,marca='',modelo='',cPuertas=0,color='',precio=0):
        self.__marca = marca
        self.__modelo = modelo
        self.__cPuertas = cPuertas
        self.__color = color
        self.__precio = precio
    def getMarca(self): return self.__marca
    def getModelo(self): return self.__modelo
    def getCantidadPuertas(self): return self.__cPuertas
    def getColor(self): return self.__color
    #GET & SET - Precio
    def getPrecio(self): return self.__precio
    def setPrecio(self,value = 0): self.__precio = value
    def importeVenta(self): pass
    def toJSON(self): pass