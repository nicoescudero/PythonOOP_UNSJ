from classes.viajero import ViajeroFrecuente

class TravelersController:
    __list = []
    
    def __init__(self,list):
        self.__list = list

    def __findTraveler(self):
        i = 0
        number = int(input('\nIngresar numero de usuario:\t'))
        index = -1
        while i < len(self.__list) :
            if number == self.__list[i].getUserNumber():
                index = i
                i = len(self.__list)
            i += 1
        return index

    def searchTravelerWithMiles(self):
        i = 0
        traveler = ViajeroFrecuente()
        miles = int(input('Ingresar cantidad de millas a buscar:\t'))
        
        traveler.acumularMillas(miles)
        while i < len(self.__list):
            if  traveler == self.__list[i]:
                print('{} {} {} Millas = {}'.format(self.__list[i].getUserNumber(),self.__list[i].getName(),self.__list[i].getSecondName(),self.__list[i].cantidadTotalMillas()))
            i+=1

    def searchTravelerAndAddMiles(self):
        i = self.__findTraveler()
        if(i != -1):
            miles = int(input('\nIngresa la cantidad de millas:\t'))
            miles + self.__list[i]
            print('SUCCESS:\tMillas Acumuludas = ',self.__list[i].cantidadTotalMillas())
        else: print('Viajero no encontrado...')

    def searchTravelerAndRedeemMiles(self):
        i = self.__findTraveler()
        if(i != -1):
            miles = int(input('\nIngresa la cantidad de millas:\t'))
            if ((self.__list[i].cantidadTotalMillas() - miles ) >= 0):
                miles - self.__list[i]
                print('SUCCESS:\tMillas Canjeadas')
                print('{} {} {} Millas = {}'.format(self.__list[i].getUserNumber(),self.__list[i].getName(),self.__list[i].getSecondName(),self.__list[i].cantidadTotalMillas()))
            else: print('FAILURE:\tLa cantidad de millas es insuficiente para canjearlas...')
        else: print('Viajero no encontrado...')