from classes.vehiculo import Vehiculo

class VehiculoUsado(Vehiculo):
    def __init__(self,marca='',modelo='',cPuertas=0,color='',precio=0,patente='',year=0,kilometraje=0):
        super().__init__(marca,modelo,cPuertas,color,precio)
        self.__patente = patente
        self.__year = year
        self.__kilometraje = kilometraje
    def getPatente(self): return self.__patente
    def getYear(self): return self.__year
    def getKilometraje(self): return self.__kilometraje
    def importeVenta(self):
        importe = 0
        antiguedad = (2023 - self.__year)/100
        precio = float(self.getPrecio())
        importe = precio - (precio * antiguedad)
        if self.__kilometraje >= 100000:
            importe -= - (precio * 0.02)
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
                patente = self.__patente,
                year = self.__year,
                kilometraje = self.__kilometraje
            )
        )
        return dictionary