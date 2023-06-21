from tkinter import *
from tkinter import ttk, messagebox

class Iva:
    def __init__(self):
        ventana = Tk()
        ventana.geometry('300x280')
        ventana.configure(bg='white')
        ventana.title('Ejercicio 2 Unidad4')
        self.__option = IntVar()
        self.__iva = StringVar()
        self.__precioIva = StringVar()
        opts = { 'padx': 10, 'pady': 10 }
        ttk.Label(ventana, text='Cálculo de IVA',background='lightblue',anchor='center').grid(row=0,column=0,columnspan=2,sticky='nswe',ipady=15,ipadx=110)
        ttk.Label(ventana,text='Precio sin IVA',background='white').grid(row=1,column=0,**opts)
        ttk.Label(ventana,text='IVA',background='white').grid(row=4,column=0,**opts)
        ttk.Label(ventana,text='Precio con IVA',background='white').grid(row=5,column=0,**opts)
        
        Radiobutton(ventana,background='white',highlightbackground='white',text='IVA 21 %',value=0,variable=self.__option).grid(row=2,column=0,padx=5,pady=5)
        Radiobutton(ventana,background='white',highlightbackground='white',text='IVA 10.5 %',value=1,variable=self.__option).grid(row=3,column=0,padx=5,pady=5)
        self.__precio = ttk.Entry(ventana,textvariable='')
        self.__precio.grid(row=1,column=1,padx=5)
        ttk.Entry(ventana,textvariable=self.__iva).grid(row=4,column=1,pady=5,padx=5)
        ttk.Entry(ventana,textvariable=self.__precioIva).grid(row=5,column=1,pady=5,padx=5)

        Button(ventana, text='Calcular IVA',command=self.calcular,background='lightgreen',
               highlightbackground='black',highlightthickness=1).grid(row=6,column=0,padx=5)
        Button(ventana, text='Salir',command=ventana.destroy,background='red',highlightbackground='black',
               highlightthickness=1,foreground='white').grid(row=6,column=1,padx=5,pady=15)
        ventana.mainloop()

    def calcular(self):
        try:
            precio=int(self.__precio.get())
            if self.__option.get() == 0:
                self.__precioIva.set(precio+(precio * 0.21))
                self.__iva.set(precio * 0.21)
            else:
                self.__precioIva.set(precio+(precio * 0.105))
                self.__iva.set(precio * 0.105)
            return
        except:
            messagebox.showerror(title='Error de Formulario',message='Completa precio sin Iva con algun número')
            return