import os
from classes.planAhorro import PlanAhorro
def main_menu():
    print('Ejercicio 5\t{}\n'.format(PlanAhorro.getConcesionaria()))
    print('1) Actualizar valores de vehiculos')
    print('2) Vehiculos disponibles / valor cuota')
    print('3) Monto a pagar para licitar vehiculo')
    print('4) Modificar cantidad de cuotas para licitar vehiculo')
    print('\n9) Salir')

def clearConsole():
    command = 'clear'
    if os.name in ('nt', 'dos'):  # If Machine is running on Windows, use cls
        command = 'cls'
    os.system(command)