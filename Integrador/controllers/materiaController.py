class MateriaController:
    def __init__(self,list = []):
        self.__list = list
    #Promedio de alumno
    def promedio(self):
        i = 0
        dni = int(input('\nIngresar DNI del alumno:\t'))
        nota = 0
        count = 0
        while i < len(self.__list):
            if dni == self.__list[i].getDni():
                nota += self.__list[i].getNota()
                count += 1
            i += 1
        if count > 0:
            print('Promedio del alumno: {}'.format(nota/count,'.2f'))
        else: print('No se encontro el DNI ingresado')
    #Listado de alumnos promocionales
    def promocionales(self):
        listado = []
        nombre = input('Ingresar nombre de la materia:\t')
        for row in self.__list:
            if nombre == row.getNombre():
                if row.getNota() >= 7:
                    listado.append([row.getDni(),row.getFecha(),row.getNota()])
        return listado