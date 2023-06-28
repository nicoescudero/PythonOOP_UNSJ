import requests,json
from tkinter import *
from tkinter import ttk, messagebox
from utils.jsonRW import ObjectEncoder
from controller.peliculaController import PeliculaController

class MainWindow:
    __lista = None
    __js = ObjectEncoder()

    def __init__(self) -> None:
        dictionary = self.__js.readJSON('movies.json')
        self.__movies = PeliculaController(self.__js.decodeDictionary(dictionary))
        self.__moviesList = self.__movies.getList()
        ventana = Tk()
        ventana.geometry('600x320')
        ventana.configure(bg='white')
        ventana.title('Ejercicio 5')
        self.__titulo = StringVar()
        self.__lenguaje = StringVar()
        self.__fecha = StringVar()
        self.__genero = StringVar()
        self.__lista = Listbox(ventana,width=25,height=5)
        self.__lista.grid(row=0,column=0)
        self.cargarLista()
        self.__lista.bind('<Double-Button>',self.itemSeleccionado)
        frame = Frame(ventana,width=50,height=10,highlightthickness=1,highlightcolor='black')
        frame.grid(row=0,column=1)
        Label(frame,textvariable=self.__titulo).grid(row=1,column=1)
        self.__txt = Text(frame,width=40,height=10)
        self.__txt.grid(row=2,column=1)
        Label(frame,textvariable=self.__lenguaje).grid(row=3,column=1)
        Label(frame,textvariable=self.__fecha).grid(row=4,column=1)
        Label(frame,textvariable=self.__genero).grid(row=5,column=1)
        Button(ventana, text='Salir',command=ventana.destroy).grid(row=1,column=0,padx=5,pady=15)
        ventana.mainloop()
    def cargarLista(self):
        count = 0
        for i in self.__moviesList:
            self.__lista.insert(count,i[0])
            count += 1
        self.__lista.grid(row=0,column=0,padx=5,pady=15)
        return
    def itemSeleccionado(self,*args):
        for i in self.__lista.curselection():
            self.__titulo.set('Titulo: {}'.format(self.__moviesList[i][0]))
            self.__txt.delete('1.0',END)
            self.__txt.insert(END,self.__moviesList[i][1])
            self.__lenguaje.set('Lenguaje: {}'.format(self.__moviesList[i][2]))
            self.__fecha.set('Estreno: {}'.format(self.__moviesList[i][3]))
            self.__genero.set('Genero ID: {}'.format(self.__moviesList[i][4]))