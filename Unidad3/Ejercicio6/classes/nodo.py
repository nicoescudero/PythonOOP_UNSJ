from classes.vUsado import VehiculoUsado

class Nodo:
    def __init__(self,vehiculo):
        self.__vehiculo = vehiculo
        self.__siguiente = None
    def setSiguiente(self,siguiente):
        self.__siguiente = siguiente
    def getSiguiente(self): return self.__siguiente
    def getDato(self):
        data = '\nModelo: {}\nCantidad de puertas: {} Precio de venta: ${}'.format(
            self.__vehiculo.getModelo(),
            self.__vehiculo.getCantidadPuertas(),
            self.__vehiculo.importeVenta())
        return data
    def getObjectType(self): return type(self.__vehiculo)
    def setPrecio(self,patente):
        if type(self.__vehiculo) == VehiculoUsado:
            if patente == self.__vehiculo.getPatente():
                precio = input('Ingresar nuevo precio:\t$')
                self.__vehiculo.setPrecio(precio)
                return True
        return False
    def getPrecio(self): return self.__vehiculo.importeVenta()
    def getAllData(self):
        data = '\nMarca: {}\tModelo: {}\nCantidad de puertas: {}\tColor: {}\nPrecio de venta: ${}'.format(
            self.__vehiculo.getMarca(), self.__vehiculo.getModelo(), self.__vehiculo.getCantidadPuertas(),
            self.__vehiculo.getColor(), self.__vehiculo.importeVenta())
        return data
    def toJSON(self): return self.__vehiculo.toJSON()
        