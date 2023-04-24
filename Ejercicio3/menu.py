import os

def main_menu():
    print('Ejercicio 3\n')
    print('1) Datos de temperatura')
    print('2) Temperatura promedio mensual')
    print('3) Mostrar valores por hora')
    print('9) Salir')

def clearConsole():
    command = 'clear'
    if os.name in ('nt', 'dos'):  # If Machine is running on Windows, use cls
        command = 'cls'
    os.system(command)