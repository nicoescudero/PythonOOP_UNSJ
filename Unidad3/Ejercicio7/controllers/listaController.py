from utils.jsonRW import ObjectEncoder
from classes.docente import Docente
from classes.docenteInvestigador import DocenteInvestigador
from classes.investigador import Investigador
from classes.personalApoyo import PersonalApoyo

class ListaController:
    def __init__(self):
        self.__myJSON = ObjectEncoder()
        dictionary = self.__myJSON.readJSON('personal.json')
        self.__lista = self.__myJSON.decodeDictionary(dictionary)
    def crearDocenteInvestigador(self):
        data = []

    def __crearDocente(self,cuil,apellido,nombre,sueldo,antiguedad):
        carrera = input('Ingresar Carrera:\t')
        cargo = input('Ingresar Cargo:\t')
        catedra = input('Ingresar Catedra:\t')
        return Docente(cuil,apellido,nombre,sueldo,antiguedad,carrera,cargo,catedra)
    def __crearDocenteInvestigador(self,cuil,apellido,nombre,sueldo,antiguedad):
        area = input('Ingresar Area\t')
        tipo = input('Ingresar Tipo\t')
        carrera = input('Ingresar Carrera:\t')
        cargo = input('Ingresar Cargo:\t')
        catedra = input('Ingresar Catedra:\t')
        categoria = input('Ingresar Categoria:\t')
        ied = int(input('Ingresar importe extra docencia:\t'))
        iei = int(input('Ingresar importe extra investigador:\t'))
        return DocenteInvestigador(cuil,apellido,nombre,sueldo,antiguedad,area,tipo,carrera,cargo,catedra,categoria,ied,iei)
    def __crearInvestigador(self,cuil,apellido,nombre,sueldo,antiguedad):
        area = input('Ingresar Area:\t')
        tipo = input('Ingresar Tipo:\t')
        return Investigador(cuil,apellido,nombre,sueldo,antiguedad,area,tipo)
    def crearPersonal(self):
        print('1)Docente\n2)Docente Investigador\n3)Investigador\n4)Personal de Apoyo')
        option = int(input('\nSelecciona una opcion:\t'))
        elemento = None
        cuil = None
        apellido = None
        nombre = None
        sueldo = None
        antiguedad = None
        if option == 1 or option == 2 or option == 3 or option == 4:
            cuil = input('Ingresar cuil:\t')
            apellido = input('Ingresar Apellido:\t')
            nombre = input('Ingresar Nombre:\t')
            sueldo = int(input('Ingresar Sueldo:\t'))
            antiguedad = int(input('Ingresar Antiguedad:\t'))
            if option == 1: elemento = self.__crearDocente(cuil,apellido,nombre,sueldo,antiguedad)
            if option == 2: elemento = self.__crearDocenteInvestigador(cuil,apellido,nombre,sueldo,antiguedad)
            if option == 3: elemento = self.__crearInvestigador(cuil,apellido,nombre,sueldo,antiguedad)
            if option == 4:
                categoria = input('Ingresar Categoria:\t')
                elemento = PersonalApoyo(cuil,apellido,nombre,sueldo,antiguedad,categoria)
        else: print('Opcion Incorrecta...')
        return elemento

    def agregarPersonal(self):
        elemento = self.__crearPersonal()
        self.__lista.agregarElemento(elemento)
    def agregarPersonalPorPosicion(self):
        p = int(input('Ingresar posicion:\t'))
        elemento = self.__crearPersonal()
        self.__lista.insertarElemento(elemento,p)
    def tipoPersonal(self):
        p = int(input('Ingresar posicion:\t'))
        print(self.__lista.mostrarElemento(p))
    def docentesInvestigadoresPorCarrera(self):
        carrera = input('Ingresar Carrera a buscar:\t')
        self.__lista.buscarDocentesI(carrera)
    def cantidadDocentesIeInvestigadores():
        element = None
    def datosAgentes(self):
        for i in self.__lista:
            print(i)
    def docentesInvestigadoresPorCategoria(self):
        element = None
    def guardarCambios(self):
        dictionary = self.__lista.toJSON()
        self.__myJSON.saveJSON(dictionary,'personal.json')