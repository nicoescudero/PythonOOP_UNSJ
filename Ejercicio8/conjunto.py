class Conjunto:
    conjuntos = []
    def __init__(self,conjuntos):
        self.__conjuntos = set(conjuntos)
    def getConjunto(self): return self.__conjuntos
    #Operator overload +
    def __add__(self,other):
        self.__conjuntos = self.__conjuntos.union(other.getConjunto())
        return self.__conjuntos
    #Operator overload -
    def __sub__(self,other):
        self.__conjuntos = self.__conjuntos.difference(other.getConjunto())
        return self.conjuntos
    #Operator overload ==
    def __eq__(self, other):
        C = other.getConjunto()
        if len(self.__conjuntos) == len(C):
            if self.__conjuntos == C: return True
            else: return False
        else: return False