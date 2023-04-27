class Ventana:
    def __init__(self,titulo = '',xVSI = 0, yVSI = 0, xVID = 0, yVID = 0):
        self.__titulo = titulo
        self.__xVSI = xVSI
        self.__yVSI = yVSI
        self.__xVID = xVID
        self.__yVID = yVID

    def mostrar(self):
        print(self.__titulo, self.__xVSI, self.__yVSI, self.__xVID, self.__yVID)
    def getTitulo(self): return self.__titulo
    def alto(self): return self.__yVSI
    def ancho(self): return self.__xVSI
    def moverDerecha(self,value):
        if((self.__xVID + value) <= 500):
            self.__xVID += value
            return True
        else: return False
    def moverIzquierda(self,value):
        if((self.__xVSI + value) >= 0):
            self.__xVSI += value
            return True
        else: return False
    def bajar(self,value = 0):
        if((self.__yVSI + value) >= 0 and (self.__yVID + value) <= 500):
            self.__yVSI -= value
            self.__yVID -= value
            return True
        else: return False
    def subir(self,value = 0):
        if((self.__yVSI + value) >= 0 and (self.__yVID + value) <= 500):
            self.__yVSI += value
            self.__yVID += value
            return True
        else: return False