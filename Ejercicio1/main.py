from utils.csv import loadFileCSV
from classes.email import email
import controllers.controllerEmail as controller

#Items a, b
address1 = email('user1','@example','.net','1234')
print(address1.retornaEmail())
#Function 1
address2 = email('','','','')
username = input('ingrese su nombre:\t')
userEmail = input('ingrese su email:\t')
address2.crearCuenta(userEmail)
print(address2.sendMessage(username,userEmail))
#Function 2 Cambio de contraseña
print('\n**************************')
print('Cambio de Contraseña...')
currentPassword = input('Ingrese su contraseña actual (si no tienes presiona enter):\t')
newPassword = input('Ingrese su nueva contraseña:\t')
response = address2.setPassword(currentPassword,newPassword)
print(response)
#Function 3, 4 & Item c
print('\n-- Carga de lista de emails --\n')
lista = loadFileCSV()
domain = input('\nIngrese el dominio que quiere buscar:\t')

controller.searchDomain(lista,domain)