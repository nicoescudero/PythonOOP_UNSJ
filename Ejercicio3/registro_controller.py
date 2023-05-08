class RegController:
    def __init__(self, list = []):
        self.__list = list
    #Para cada variable de mostrar el menor y mayor valor junto con su dia y hora
    def maxAndMin(self):
        maxT = self.__list[0][0].getTemperatura()
        maxH = self.__list[0][0].getHumedad()
        maxP = self.__list[0][0].getPresionAtmoseferica()
        minT = maxT
        minH = maxH
        minP = maxP
        dayMT = 0
        dayMH = 0
        dayMP = 0
        daymT = 0
        daymH = 0
        daymP = 0
        hourMT = 0
        hourMP = 0
        hourMH = 0
        hourmT = 0
        hourmH = 0
        hourmP = 0
        day = 1
        for dia in self.__list:
            hour = 0
            for hora in dia:
                temperatura = hora.getTemperatura()
                humedad = hora.getHumedad()
                presion = hora.getPresionAtmoseferica()
                if temperatura > maxT: 
                    dayMT = day
                    hourMT = hour
                    maxT = temperatura
                else:
                    daymT = day
                    hourmT = hour
                    minT = temperatura
                if humedad > maxH:
                    dayMH = day
                    hourMH = hour
                    maxH = humedad
                else:
                    daymH = day
                    hourmH = hourmH
                    minH = humedad
                if presion > maxP:
                    dayMP = day
                    hourMP = hour
                    maxP = presion
                else:
                    daymP = day
                    hourmP = hour
                    minP = presion
                hour += 1
            day += 1
        print('Temperatura:\nMaxima = {} Dia: {} Hora: {}\nMinima = {} Dia: {} Hora: {}'.format(maxT,dayMT,hourMT,minT,daymT,hourmT))
        print('\nHumedad:\nMaxima = {} Dia: {} Hora: {}\nMinima = {} Dia: {} Hora: {}'.format(maxH,dayMH,hourMH,minH,daymH,hourmH))
        print('\nPresion atmosferica\nMaxima = {} Dia: {} Hora: {}\nMinima = {} Dia: {} Hora: {}'.format(maxP,dayMP,hourMP,minP,daymP,hourmP))
    #Temperatura promedio
    def temperaturaPromedio(self):
        tProm = [0 for colum in range(24)]
        for dia in self.__list:
            h = 0
            for hora in dia:
                tProm[h] += hora.getTemperatura()
                h += 1
        print(tProm)
        print('\nTemperatura promedio para cada hora...\n')
        h = 0
        for t in tProm:
            print('Hora: {}hs Temperatura: {}'.format(h,t/2),)
            h += 1
    #Busquedad de los valores de las variables
    def buscarDiaYVariables(self):
        dia = int(input('Ingresar dia:\t'))
        dia = dia -1
        i = 0
        while i < len(self.__list[dia]):
            print('\nHora: {}hs'.format(i))
            print('Temperatura: {}\tHumedad: {}\tPresion Atmosferica: {}'.format(self.__list[dia][i].getTemperatura(),self.__list[dia][i].getHumedad(),self.__list[dia][i].getPresionAtmoseferica()))
            i += 1
    