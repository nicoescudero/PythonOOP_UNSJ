import os

def main_menu():
    print('Ejercicio 5\n')
    print('1) Actualizar valores de vehiculos')
    print('2) Vehiculos disponibles / valor cuota')
    print('3) Monto a pagar para licitar vehiculo')
    print('4) Modificar cantidad de cuotas para licitar vehiculo')
    print('5) Importe de todos los vehiculos')
    print('\n9) Salir')

def clearConsole():
    command = 'clear'
    if os.name in ('nt', 'dos'):  # If Machine is running on Windows, use cls
        command = 'cls'
    os.system(command)