class Registro:
    __temperatura = 0
    __humedad = 0
    __presionAtmosferica = 0
    def __init__(self,temperatura,humedad,presionAtmosferica):
        self.__temperatura = temperatura
        self.__humedad = humedad
        self.__presionAtmosferica = presionAtmosferica
    #Obetener temperatura
    def getTemperatura(self): return self.__temperatura
    #Obtener humedad
    def getHumedad(self): return self.__humedad
    #Obtener presion atmosferica
    def getPresionAtmoseferica(self): return self.__presionAtmosferica
    