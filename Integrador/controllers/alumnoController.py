import numpy as np
from classes.alumno import Alumno
class AlumnoController:
    def __init__(self,list = []):
        self.__alumnos = np.array(list,dtype=Alumno)
    #Informacion de alumnos promocionales
    def mostrar(self,promocionales = []):
        print('Alumnos...\n')
        i = 0
        while i < len(promocionales):
            j = 0
            while j < len(self.__alumnos):
                if promocionales[i][0] == self.__alumnos[j].getDni():
                    print('{}\t{}\t{}\t{}\t{}\t{}'.format(promocionales[i][0], self.__alumnos[j].getApellido(),self.__alumnos[j].getNombre(),promocionales[i][1],promocionales[i][2],self.__alumnos[j].getAño()))
                    j = len(self.__alumnos)
                j += 1
            i += 1
    #Listado ordenado de alumnos
    def listado(self):
        for j in range(1,len(self.__alumnos)):
            alumno = self.__alumnos[j]
            apellido = self.__alumnos[j].getApellido()
            i = j -1
            while i >= 0 and apellido < self.__alumnos[i].getApellido():
                self.__alumnos[i + 1] = self.__alumnos[i]
                i -= 1
            self.__alumnos[i + 1] = alumno
        for i in range(1,len(self.__alumnos)):
            alumno = self.__alumnos[i]
            year = self.__alumnos[i].getAño()
            j = i -1
            while j >= 0 and year < self.__alumnos[j].getAño():
                self.__alumnos[j + 1] = self.__alumnos[j]
                j -= 1
            self.__alumnos[j + 1] = alumno
        print('\n')
        for row in self.__alumnos:
            print(row.getAño(),row.getApellido(),row.getNombre())
        