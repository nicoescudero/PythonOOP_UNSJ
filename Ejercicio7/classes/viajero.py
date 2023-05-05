class ViajeroFrecuente:
    #Item a
    def __init__(self,number=0,dni=0,name='',secondName='',miles=0):
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
    #Operator overload ==
    def __eq__(self, other):
        if type(self) == type(other):
            if self.__millasAcumuladas == other.cantidadTotalMillas(): return True
        else:
            if type(other) == int or type(other) == float:
                if self.__millasAcumuladas == other: return True
                else: return False
            else: return False
    #Operator overload +
    def __radd__(self,other):
        if type(self) == type(other):
            self.__millasAcumuladas += other.cantidadTotalMillas()
            return self.__millasAcumuladas
        elif type(other) == int or type(other) == float:
            self.__millasAcumuladas += other
            return self.__millasAcumuladas
    #Operator overload -
    def __rsub__(self,other):
        if type(self) == type(other):
            self.__millasAcumuladas -= other.cantidadTotalMillas()
            return self.__millasAcumuladas
        elif type(other) == int or type(other) == float:
            self.__millasAcumuladas -= other
            return self.__millasAcumuladas    