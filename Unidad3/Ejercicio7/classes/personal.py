class Personal:
    def __init__(self,**kwargs):
        self.__cuil = kwargs['cuil']
        self.__apellido = kwargs['apellido']
        self.__nombre = kwargs['nombre']
        self.__sueldo = kwargs['sueldo']
        self.__antiguedad = kwargs['antiguedad']
    def getCuil(self): return self.__cuil
    def getApellido(self): return self.__apellido
    def getNombre(self): return self.__nombre
    def getSueldo(self): return self.__sueldo
    def getAntiguedad(self): return self.__antiguedad
    def mostrarSueldo(self): pass
    def mostrarDatos(self): pass
    def getObjectType(self): pass