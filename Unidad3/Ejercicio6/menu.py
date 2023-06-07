import os
from colorama import Fore, Back, Style

def main_menu():
    print('*****************************************')
    print('*' + Fore.YELLOW+Back.LIGHTCYAN_EX+Style.BRIGHT + '\tEjercicio 2' + Back.RESET+Style.RESET_ALL + '\n*')
    print('*\t 1)Insertar vehiculo en determinada posicion (Crear e insertar)')
    print('*\t 2)Agregar vehiculo a la coleccion')
    print('*\t 3)Mostar tipo de objeto en determinada posicion')
    print('*\t 4)Modificar precio de vehiculo usado (Busqueda por patente)')
    print('*\t 5)Vehiculo mas economico de la concesionaria')
    print('*\t 6)Datos de todos los vehiculos de la concesionaria')
    print('*\t 9)Salir y Guardar Cambios\n*')
    print('*****************************************')

def clearConsole():
    command = 'clear'
    if os.name in ('nt', 'dos'):  # If Machine is running on Windows, use cls
        command = 'cls'
    os.system(command)