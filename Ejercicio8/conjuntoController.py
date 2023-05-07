
from conjunto import Conjunto
class ConjuntoController:
    def __init__(self) -> None:
        pass

    def __cargarConjuntos(self):
        i = 0
        j = 0
        conjuntoA = []
        conjuntoB = []
        tA = int(input('Ingrese tamaño del conjunto A:\t'))
        tB = int(input('Ingrese tamaño del conjunto B:\t'))
        print('\nCARGA del Conjunto A...')
        while i < tA:
            a = input('Ingresar elemento:\t')
            conjuntoA.append(int(a))
            i+=1
        print('\nCARGA del Conjunto B...')
        while j < tB:
            b = input('Ingresar elemento:\t')
            conjuntoB.append(int(b))
            j+=1
        return [conjuntoA,conjuntoB]

    def __conjuntosCargados(self,a,b):
        print('Conjunto A...')
        print(a.getConjunto())
        print('Conjunto B...')
        print(b.getConjunto())
    #Union de conjuntos
    def union(self):
        response = self.__cargarConjuntos()
        a = Conjunto(response[0])
        b = Conjunto(response[1])
        self.__conjuntosCargados(a,b)
        print('\nConjunto A + Conjunto B')
        a+b
        print(a.getConjunto())
    #Diferencia de conjuntos
    def diferencia(self):
        response = self.__cargarConjuntos()
        a = Conjunto(response[0])
        b = Conjunto(response[1])
        self.__conjuntosCargados(a,b)
        print('\nConjunto A - Conjunto B')
        a-b
        print(a.getConjunto())
    #Igualdad de conjuntos
    def igualdad(self):
        response = self.__cargarConjuntos()
        a = Conjunto(response[0])
        b = Conjunto(response[1])
        self.__conjuntosCargados(a,b)
        print('\nConjunto A = Conjunto B')
        if a == b:
            print('Los conjuntos son iguales')
        else: print('Los conjuntos son distintos')