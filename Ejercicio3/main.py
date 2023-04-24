from colorama import init, Fore
from menu import main_menu, clearConsole
from utils.txtReader import loadFileTXT

init()
flag = True
option = 0

while flag:
    main_menu()
    option = int(input(Fore.LIGHTGREEN_EX+'\tSeleccionar una opcion:\t'+Fore.RESET))
    if(option != 1 and option != 2 and option != 3 and option != 9):
        print('Ingresa una de las opciones disponibles.')
        input()
        clearConsole()
    elif option == 9 :
        flag = False
        clearConsole()
    else:
        input()
        clearConsole()
