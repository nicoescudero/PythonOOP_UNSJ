import os
from colorama import Fore, Back, Style

def main_menu():
    print('*****************************************')
    print('*' + Fore.YELLOW+Back.LIGHTCYAN_EX+Style.BRIGHT + '\tEjercicio 7' + Back.RESET+Style.RESET_ALL + '\n*')
    print('*\t 1)Agregar Agente a coleccion')
    print('*\t 2)Insertar Agente por Posicion (Crear e insertar)')
    print('*\t 3)Mostar tipo de Agente en determinada posicion')
    print('*\t 4)Agentes que se desempeñan como Docentes Investigadores en determinada carrera')
    print('*\t 5)Cantidad de Agentes que son Docentes Investigadores e Investigadores')
    print('*\t 6)Datos de todos los Agentes')
    print('*\t 7)Informacion de Docentes Investigadores (Busqueda por Categoria)')
    print('*\t 9)Salir y Guardar Cambios\n*')
    print('*****************************************')

def clearConsole():
    command = 'clear'
    if os.name in ('nt', 'dos'):  # If Machine is running on Windows, use cls
        command = 'cls'
    os.system(command)