from model.pelicula import Pelicula

class PeliculaController:
    def __init__(self,lista = []):
        self.__lista = lista
    def getList(self):
        peliculas = []
        for i in self.__lista:
            item = [i.getTitulo(),i.getResumen(),i.getLenguaje(),i.getFecha(),i.getGenero()]
            peliculas.append(item)
        return peliculas