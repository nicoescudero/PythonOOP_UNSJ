from classes.vehiculo import Vehiculo

class VehiculoNuevo(Vehiculo):
    def __init__(self,marca='',modelo='',cPuertas=0,color='',precio=0,version=''):
        super().__init__(marca,modelo, cPuertas, color, precio)
        self.__version = version
    def getVersion(self): return self.__version
    def importeVenta(self):
        importe = 0
        precio = float(self.getPrecio())
        importe = precio + (precio * 0.1)
        if self.__version == 'Full':
            importe += (precio * 0.02)
        return importe
    def toJSON(self):
        dictionary = dict(
            __class__ = self.__class__.__name__,
            __atributos__=dict(
                marca = self.getMarca(),
                modelo = self.getModelo(),
                cPuertas = self.getCantidadPuertas(),
                color = self.getColor(),
                precio = self.getPrecio(),
                version = self.__version
            )
        )
        return dictionary