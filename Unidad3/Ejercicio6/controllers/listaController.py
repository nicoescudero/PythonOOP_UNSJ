from utils.jsonRW import ObjectEncoder
from classes.vNuevo import VehiculoNuevo
from classes.vUsado import VehiculoUsado
import json

class ListaController:
    def __init__(self):
        self.__myJSON = ObjectEncoder()
        dictionary = self.__myJSON.readJSON('vehiculos.json')
        self.__lista = self.__myJSON.decodeDictionary(dictionary)
    def __crearVehiculo(self):
        print('\n1)Vehiculo Nuevo\n2)Vehiculo Usado\n')
        option = int(input('Ingresa una opcion:\t'))
        vehiculo = None
        if option == 1:
            marca = input('Ingresar marca:\t')
            modelo = input('Ingresar modelo:\t')
            cPuertas = int(input('Ingresar cantidad de puertas:\t'))
            color = input('Ingresar color:\t')
            precio = int(input('Ingresar precio base:\t'))
            version = input('Ingresar Version:\t')
            vehiculo = VehiculoNuevo(marca,modelo,cPuertas,color,precio,version)
        else:
            marca = input('Ingresar marca:\t')
            modelo = input('Ingresar modelo:\t')
            cPuertas = int(input('Ingresar cantidad de puertas:\t'))
            color = input('Ingresar color:\t')
            precio = int(input('Ingresar precio base:\t'))
            patente = input('Ingresar patente:\t')
            year = int(input('Ingresar año:\t'))
            kilometraje = int(input('Ingresar kilometraje:\t'))
            vehiculo = VehiculoUsado(marca,modelo,cPuertas,color,precio,patente,year,kilometraje)
        return vehiculo
    def insertarVehiculoEnPosicion(self):
        elemento = self.__crearVehiculo()
        p = int(input('Ingresar posicion:\t'))
        self.__lista.insertarElemento(elemento,p)
    def agregarVehiculoAColeccion(self):
        elemento = self.__crearVehiculo()
        self.__lista.agregarElemento(elemento)
    def mostrarTipoElemento(self):
        p = int(input('Ingresar posicion:\t'))
        print(self.__lista.mostrarElemento(p))
    def buscarYModificarPrecio(self):
        patente = input('Ingresar patente:\t')
        self.__lista.buscarPatente(patente)
    def vehiculoMasEconomico(self):
        self.__lista.vehiculoEconomico()
    def allDataList(self):
        for i in self.__lista:
            print(i)
    def guardarCambios(self):
        dictionary = self.__lista.toJSON()
        self.__myJSON.saveJSON(dictionary,'vehiculos.json')