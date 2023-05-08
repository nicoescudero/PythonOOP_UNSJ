class Alumno:
    def __init__(self,dni=0,apellido='',nombre='',carrera='',año=''):
        self.__dni = dni
        self.__apellido = apellido
        self.__nombre = nombre
        self.__carrera = carrera
        self.__año = año
    #GET & SET - DNI
    def getDni(self): return self.__dni
    def setDni(self,value): self.__dni = value
    #GET & SET - Apellido
    def getApellido(self): return self.__apellido
    def setApellido(self,value): self.__apellido = value
    #GET & SET - Nombre
    def getNombre(self): return self.__nombre
    def setNombre(self,value): self.__nombre = value
    #GET & SET - Carrera
    def getCarrera(self): return self.__carrera
    def setCarrera(self,value): self.__carrera = value
    #GET & SET - Año
    def getAño(self): return self.__año
    def setAño(self,value): self.__año = value
    #Operator Overload <
    def __lt__(self,other):
        if self.__año < other.getAño(): return True
        else: return False