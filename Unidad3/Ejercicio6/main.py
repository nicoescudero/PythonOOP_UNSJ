from colorama import init,Fore
from utils.jsonRW import ObjectEncoder
from menu import main_menu,clearConsole
from controllers.listaController import ListaController

init()
listaCtrl = ListaController()
flag = True
option = None
while(flag != False):
    main_menu()
    option = int(input(Fore.LIGHTGREEN_EX+'\tSeleccionar una opcion:\t'+Fore.RESET))
    if option == 1: listaCtrl.insertarVehiculoEnPosicion()
    if option == 2: listaCtrl.agregarVehiculoAColeccion()
    if option == 3: listaCtrl.mostrarTipoElemento()
    if option == 4: listaCtrl.buscarYModificarPrecio()
    if option == 5: listaCtrl.vehiculoMasEconomico()
    if option == 6: listaCtrl.allDataList()
    if(option != 1 and option != 2 and option != 3 and option != 4 and option != 5 and option != 6 and option != 9):
        print('Ingresa una de las opciones disponibles.')
        input()
        clearConsole()
    elif option == 9 :
        flag = False
        clearConsole()
        listaCtrl.guardarCambios() 
    else: 
        input()
        clearConsole()
