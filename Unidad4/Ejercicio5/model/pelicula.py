class Pelicula:
    def __init__(self,titulo='',resumen='',lenguajeOriginal='',fechaEstreno='',genero=''):
        self.__titulo = titulo
        self.__resumen = resumen
        self.__lenguajeOriginal = lenguajeOriginal
        self.__fechaEstreno = fechaEstreno
        self.__genero = genero
    def getTitulo(self): return self.__titulo
    def getResumen(self): return self.__resumen
    def getLenguaje(self): return self.__lenguajeOriginal
    def getFecha(self): return self.__fechaEstreno
    def getGenero(self): return self.__genero