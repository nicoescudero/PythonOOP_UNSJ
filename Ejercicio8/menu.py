import os
from colorama import Fore, Back, Style

def main_menu():
    print('*****************************************')
    print('*' + Fore.YELLOW+Back.LIGHTCYAN_EX+Style.BRIGHT + '\tEjercicio 8' + Back.RESET+Style.RESET_ALL + '\n*')
    print('*\t 1)Unir conjuntos')
    print('*\t 2)Diferencia de conjuntos')
    print('*\t 3)Conjuntos iguales')
    print('\n*\t 9)Salir\n*')
    print('*****************************************')



def clearConsole():
    command = 'clear'
    if os.name in ('nt', 'dos'):  # If Machine is running on Windows, use cls
        command = 'cls'
    os.system(command)