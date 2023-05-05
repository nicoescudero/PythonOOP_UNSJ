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

    def findTravelerWithMoreMiles(self):
        traveler = self.__list[0]
        i = 1
        while i < len(self.__list):
            if self.__list[i] > traveler:
                traveler = self.__list[i]
            i+=1
        print('Viajero con mayor cantidad de millas...')
        print('{} {} {} Millas = {}'.format(traveler.getUserNumber(),traveler.getName(),traveler.getSecondName(),traveler.cantidadTotalMillas()))

    def searchTravelerAndAddMiles(self):
        i = self.__findTraveler()
        if(i != -1):
            miles = int(input('\nIngresa la cantidad de millas:\t'))
            self.__list[i] + miles
            print('SUCCESS:\tMillas Acumuludas = ',self.__list[i].cantidadTotalMillas())
        else: print('Viajero no encontrado...')

    def searchTravelerAndRedeemMiles(self):
        i = self.__findTraveler()
        if(i != -1):
            miles = int(input('\nIngresa la cantidad de millas:\t'))
            if ((self.__list[i].cantidadTotalMillas() - miles ) >= 0):
                self.__list[i] - miles
                print('SUCCESS:\tMillas Canjeadas\n\t\tMillas = ',self.__list[i].cantidadTotalMillas())
            else: print('FAILURE:\tLa cantidad de millas es insuficiente para canjearlas...')
        else: print('Viajero no encontrado...')