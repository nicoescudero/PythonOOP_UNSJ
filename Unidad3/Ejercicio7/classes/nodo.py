from classes.docenteInvestigador import DocenteInvestigador

class Nodo:
    def __init__(self,personal):
        self.__personal = personal
        self.__siguiente = None
    def setSiguiente(self,siguiente):
        self.__siguiente = siguiente
    def getSiguiente(self): return self.__siguiente
    def getDato(self):
        data = '{} {}\tSueldo: ${}'.format(
            self.__personal.getApellido(),
            self.__personal.getNombre(),
            self.__personal.getSueldo())
        return data
    def getObjectType(self):
        return self.__personal.getObjectType()
    def dataDocenteI(self,carrera):
        if type(self.__personal) is DocenteInvestigador:
            if self.__personal.getCarrera() == carrera:
                self.__personal.mostrarDatos()
    def toJSON(self): return self.__personal.toJSON()