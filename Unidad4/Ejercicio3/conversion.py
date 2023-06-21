import requests,json
from tkinter import *
from tkinter import ttk, messagebox
class Conversion:
    __precioDolar=0
    def __init__(self) -> None:
        self.cargarPrecioDolar()
        ventana = Tk()
        ventana.geometry('300x120')
        ventana.configure(bg='white')
        ventana.title('Conversor de Moneda')
        self.__pesos = StringVar()
        self.__cantidad = StringVar()
        self.__pesos.set('Es equivalente a $ pesos')
        self.__cantidad.set('')
        self.__cantidad.trace('w',self.calcular)
        ttk.Entry(ventana,textvariable=self.__cantidad,width=5).grid(row=0,column=0,pady=10)
        ttk.Label(ventana, text='dólares',background='white').grid(row=0,column=1,padx=0,ipadx=0)
        ttk.Label(ventana,textvariable=self.__pesos,background='white').grid(row=1,column=0)
        Button(ventana, text='Salir',command=ventana.destroy).grid(row=6,column=1,padx=5,pady=15)
        ventana.mainloop()
    #Carga valor del dolar desde la API
    def cargarPrecioDolar(self):
        response = requests.get('https://www.dolarsi.com/api/api.php?type=dolar')
        diccionario = json.loads(response.text)[0]
        resultado = float((diccionario['casa']['venta']).replace(",","."))
        self.__precioDolar = int(resultado)
        return
    #Conversion a pesos
    def calcular(self,*args):
        try:
            if self.__cantidad.get() != '':
                total=int(self.__cantidad.get()) * self.__precioDolar
                self.__pesos.set('Es equivalente a ${:.2f} pesos'.format(total))
                return
            else:
                self.__pesos.set('Es equivalente a $ pesos')
                return
        except:
            messagebox.showerror(title='Error de Formulario',message='Debes ingresar números')
            return