class RegController:
    def __init__(self, list = []):
        self.__list = list
    #Para cada variable de mostrar el menor y mayor valor junto con su dia y hora
    def maxAndMin(self):
        t = [self.__list[0][0].getTemperatura(),0,0,self.__list[0][0].getTemperatura(),0,0]
        h = [self.__list[0][0].getHumedad(),0,0,self.__list[0][0].getHumedad(),0,0]
        p = [self.__list[0][0].getHumedad(),0,0,self.__list[0][0].getHumedad(),0,0]
        day = 1
        for dia in self.__list:
            hour = 0
            for hora in dia:
                temperatura = hora.getTemperatura()
                humedad = hora.getHumedad()
                presion = hora.getPresionAtmoseferica()
                if temperatura > t[0]: 
                    t[0] = temperatura
                    t[1] = day
                    t[2] = hour
                else:
                    t[3] = temperatura
                    t[4] = day
                    t[5] = hour
                if humedad > h[0]:
                    h[0] = humedad
                    h[1] = day
                    h[2] = hour
                else:
                    h[3] = humedad
                    h[4] = day
                    h[5] = hour
                if presion > p[0]:
                    p[0] = presion
                    p[1] = day
                    p[2] = hour
                else:
                    p[3] = presion
                    p[4] = day
                    p[5] = hour
                hour += 1
            day += 1
        print('Temperatura:\nMaxima = {} Dia: {} Hora: {}\nMinima = {} Dia: {} Hora: {}'.format(t[0],t[1],t[2],t[3],t[4],t[5]))
        print('\nHumedad:\nMaxima = {} Dia: {} Hora: {}\nMinima = {} Dia: {} Hora: {}'.format(h[0],h[1],h[2],h[3],h[4],h[5]))
        print('\nPresion atmosferica\nMaxima = {} Dia: {} Hora: {}\nMinima = {} Dia: {} Hora: {}'.format(p[0],p[1],p[2],p[3],p[4],p[5]))
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
    