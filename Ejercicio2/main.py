from colorama import init,Fore
from menu import main_menu,clearConsole
from utils.csvReader import loadFileCSV
from controller.travelers_controller import TravelersController

init()
TController = TravelersController(loadFileCSV())
flag = True
option = None
while(flag != False):
    main_menu()
    option = int(input(Fore.LIGHTGREEN_EX+'\tSeleccionar una opcion:\t'+Fore.RESET))
    if option == 1: TController.searchTravelerAndGetMiles()
    if option == 2: TController.searchTravelerAndAddMiles()
    if option == 3: TController.searchTravelerAndRedeemMiles()
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