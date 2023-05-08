from colorama import init,Fore
from menu import main_menu,clearConsole
from utils.csvReader import loadFileCSV
from controllers.alumnoController import AlumnoController
from controllers.materiaController import MateriaController

init()
estudiantesCtrl = AlumnoController(loadFileCSV('alumnos.csv'))
materiaCtrl = MateriaController(loadFileCSV('materiasAprobadas.csv'))
flag = True
option = 0

while flag:
    main_menu()
    option = int(input(Fore.LIGHTGREEN_EX+'\tSeleccionar una opcion:\t'+Fore.RESET))
    if option == 1: materiaCtrl.promedio()
    if option == 2:
        a = materiaCtrl.promocionales()
        estudiantesCtrl.mostrar(a)
    if option == 3: estudiantesCtrl.listado()
    if(option != 1 and option != 2 and option != 3 and option != 4 and option != 5 and option != 9):
        print('Ingresa una de las opciones disponibles.')
        input()
        clearConsole()
    elif option == 9 : 
        flag = False
        clearConsole()
    else: 
        input()
        clearConsole()