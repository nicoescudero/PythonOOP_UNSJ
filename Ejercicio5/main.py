from colorama import init,Fore
from menu import main_menu,clearConsole
from utils.csvReader import loadFileCSV
from controllers.planController import PlanController

init()

controller = PlanController(loadFileCSV())
flag = True
option = 0

while flag:
    main_menu()
    option = int(input(Fore.LIGHTGREEN_EX+'\tSeleccionar una opcion:\t'+Fore.RESET))
    if option == 1: controller.actualizarValorVehiculo()
    if option == 2: controller.vehiculosDisponibles()
    if option == 3: controller.monto_a_Pagar()
    if option == 4: controller.modificar_Cantidad_Cuotas()
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