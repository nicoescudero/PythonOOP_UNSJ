class ViajeroFrecuente:
    __numero = 0
    __dni = 0
    __nombre = ''
    __apellido = ''
    __millasAcumuladas = 0
    #Item a
    def __init__(self,number,dni,name,secondName,miles):
        self.__numero = number
        self.__dni = dni
        self.__nombre = name
        self.__apellido = secondName
        self.__millasAcumuladas = miles
    #Item b
    def getUserNumber(self): return self.__numero
    def cantidadTotalMillas(self): return self.__millasAcumuladas
    #Item c
    def acumularMillas(self, quantiti):
        self.__millasAcumuladas += quantiti
        return self.__millasAcumuladas
    #Item d
    def canjearMillas(self, quantiti):
        if quantiti <= self.__millasAcumuladas:
            self.__millasAcumuladas -= quantiti
            return True
        else:
            return False
    def getName(self): return self.__nombre
    def getSecondName(self): return self.__apellido
    def getDni(self): return self.__dni 
    #Operator overload >
    def __gt__(self, other):
        if self.__millasAcumuladas > other.cantidadTotalMillas():
            return True
        else: return False
    #Operator overload +
    def __add__(self,value):
        self.__millasAcumuladas += value
        return self.__millasAcumuladas
    #Operator overload -
    def __sub__(self,value):
        self.__millasAcumuladas -= value
        return self.__millasAcumuladas