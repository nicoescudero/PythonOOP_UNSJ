from tkinter import *
from tkinter import ttk, messagebox

class IPC:
    def __init__(self):
        ventana = Tk()
        self.__message = StringVar()
        ventana.geometry('600x250')
        ventana.configure(bg='white')
        ventana.title('Calculadora IPC')
        opts = { 'ipadx': 10, 'ipady': 10 , 'sticky': 'nswe' }
        ttk.Label(ventana,text='Item',background='white').grid(row=0,column=0,**opts)
        ttk.Label(ventana,text='Cantidad',background='white').grid(row=0,column=1,**opts)
        ttk.Label(ventana,text='Precio año base',background='white').grid(row=0,column=2,**opts)
        ttk.Label(ventana,text='Precio año actual',background='white').grid(row=0,column=3,**opts)
        ttk.Label(ventana,text='Vestimenta',background='white').grid(row=1,column=0,**opts)
        ttk.Label(ventana,text='Alimentos',background='white').grid(row=2,column=0,**opts)
        ttk.Label(ventana,text='Educacion',background='white').grid(row=3,column=0,**opts)
        
        self.__vestimentaC = ttk.Entry(ventana,textvariable='')
        self.__vestimentaC.grid(row=1,column=1,padx=5)

        self.__vestimentaPAB = ttk.Entry(ventana,textvariable='')
        self.__vestimentaPAB.grid(row=1,column=2,padx=5)

        self.__vestimentaPAA = ttk.Entry(ventana,textvariable='')
        self.__vestimentaPAA.grid(row=1,column=3,padx=5)

        self.__alimentosC = ttk.Entry(ventana,textvariable='')
        self.__alimentosC.grid(row=2,column=1,padx=5)

        self.__alimentosPAB = ttk.Entry(ventana,textvariable='')
        self.__alimentosPAB.grid(row=2,column=2,padx=5)
        
        self.__alimentosPAA = ttk.Entry(ventana,textvariable='')
        self.__alimentosPAA.grid(row=2,column=3,padx=5)

        self.__educacionC = ttk.Entry(ventana,textvariable='')
        self.__educacionC.grid(row=3,column=1,padx=5)

        self.__educacionPAB = ttk.Entry(ventana,textvariable='')
        self.__educacionPAB.grid(row=3,column=2,padx=5)

        self.__educacionPAA = ttk.Entry(ventana,textvariable='')
        self.__educacionPAA.grid(row=3,column=3,padx=5)

        ttk.Button(ventana, text='Salir',command=ventana.destroy).grid(row=4,column=1,padx=5)
        ttk.Button(ventana, text='Calcular IPC',command=self.calcular).grid(row=4,column=2,padx=5)
        ttk.Label(ventana,text='IPC %',background='white').grid(row=5,column=0,sticky=W)
        self.myLabel=ttk.Label(ventana,textvariable=self.__message,background='white')
        self.myLabel.grid(row=5,column=1,sticky=(W,S))
        ventana.mainloop()
    #Calcular IPC
    def calcular(self):
        try:
            #TOTAL CBAB (Canasta base año base)
            vestimentaPAB = int(self.__vestimentaC.get()) * int(self.__vestimentaPAB.get())
            alimentosPAB = int(self.__alimentosC.get()) * int(self.__alimentosPAB.get())
            educacionPAB = int(self.__educacionC.get()) * int(self.__educacionPAB.get())
            totalCBAB = vestimentaPAB + alimentosPAB + educacionPAB
            #TOTAL CBAA (Canasta base año actual)
            vestimentaPAA = int(self.__vestimentaC.get()) * int(self.__vestimentaPAB.get())
            alimentosPAA = int(self.__alimentosC.get()) * int(self.__alimentosPAA.get())
            educacionPAA = int(self.__educacionC.get()) * int(self.__educacionPAA.get())
            totalCBAA = vestimentaPAA + alimentosPAA + educacionPAA
            #TOTAL
            totalCB = totalCBAA / totalCBAB
            total = '{:.2f} %'.format(totalCB * 100)
            self.__message.set(total)
            return
        except:
            messagebox.showerror(title='Error de Formulario',message='Completa todos los campos con numeros')
            return