class Materia:
    def __init__(self,dni=0,nombre='',fecha='',nota=0,aprobacion=''):
        self.__dni = dni
        self.__nombre = nombre
        self.__fecha = fecha
        self.__nota = nota
        self.__aprobacion = aprobacion
    #GET & SET - DNI
    def getDni(self): return self.__dni
    def setDni(self,value): self.__dni = value
    #GET & SET - Nombre
    def getNombre(self): return self.__nombre
    def setNombre(self,value): self.__nombre = value
    #GET & SET - Fecha
    def getFecha(self): return self.__fecha
    def setFecha(self,value): self.__fecha = value
    #GET & SET - Nota
    def getNota(self): return self.__nota
    def setNota(self,value): self.__nota = value
    #GET & SET - Aprobacion
    def getAprobacion(self): return self.__aprobacion
    def setAprobacion(self,value): self.__aprobacion = value