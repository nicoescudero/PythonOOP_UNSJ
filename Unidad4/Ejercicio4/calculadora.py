from tkinter import *
from tkinter import ttk
from functools import partial
from imaginario import Imaginario
class Calculadora(object):
    __ventana=None
    __operador=None
    __panel=None
    __operadorAux=None
    __operadorImg=None
    __primerOperando=None
    __primerOperandoImg=None
    __segundoOperando=None
    __segundoOperandoImg=None
    def __init__(self):
        self.__ventana = Tk()
        self.__ventana.title('Tk-Calculadora')
        mainframe = ttk.Frame(self.__ventana, padding="3 10 3 10")
        mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
        mainframe.columnconfigure(0, weight=1)
        mainframe.rowconfigure(0, weight=1)
        mainframe['borderwidth'] = 2
        mainframe['relief'] = 'sunken'
        self.__panel = StringVar()
        self.__operador=StringVar()
        self.__operadorAux=None
        operatorEntry=ttk.Entry(mainframe, width=10, textvariable=self.__operador, justify='center', state='disabled')
        operatorEntry.grid(column=1, row=1, columnspan=1, sticky=(W,E))
        panelEntry = ttk.Entry(mainframe, width=20, textvariable=self.__panel, justify='right',state='disabled')
        panelEntry.grid(column=2, row=1, columnspan=2, sticky=(W, E))
        ttk.Button(mainframe, text='1', command=partial(self.ponerNUMERO, '1')).grid(column=1, row=3, sticky=W)
        ttk.Button(mainframe, text='2', command=partial(self.ponerNUMERO,'2')).grid(column=2, row=3, sticky=W)
        ttk.Button(mainframe, text='3', command=partial(self.ponerNUMERO,'3')).grid(column=3, row=3, sticky=W)
        ttk.Button(mainframe, text='4', command=partial(self.ponerNUMERO,'4')).grid(column=1, row=4, sticky=W)
        ttk.Button(mainframe, text='5', command=partial(self.ponerNUMERO,'5')).grid(column=2, row=4, sticky=W)
        ttk.Button(mainframe, text='6', command=partial(self.ponerNUMERO,'6')).grid(column=3, row=4, sticky=W)
        ttk.Button(mainframe, text='7', command=partial(self.ponerNUMERO,'7')).grid(column=1, row=5, sticky=W)
        ttk.Button(mainframe, text='8', command=partial(self.ponerNUMERO,'8')).grid(column=2, row=5, sticky=W)
        ttk.Button(mainframe, text='9', command=partial(self.ponerNUMERO,'9')).grid(column=3, row=5, sticky=W)
        ttk.Button(mainframe, text='0', command=partial(self.ponerNUMERO, '0')).grid(column=1, row=6, sticky=W)
        ttk.Button(mainframe, text='i', command=partial(self.ponerNUMERO, 'i')).grid(column=3, row=8, sticky=W)
        ttk.Button(mainframe, text='+', command=partial(self.ponerOPERADOR, '+')).grid(column=2, row=6, sticky=W)
        ttk.Button(mainframe, text='-', command=partial(self.ponerOPERADOR, '-')).grid(column=3, row=6, sticky=W)
        ttk.Button(mainframe, text='*', command=partial(self.ponerOPERADOR, '*')).grid(column=1, row=7, sticky=W)
        ttk.Button(mainframe, text='/', command=partial(self.ponerOPERADOR, '/')).grid(column=2, row=7, sticky=W)
        ttk.Button(mainframe, text='=', command=partial(self.ponerOPERADOR, '=')).grid(column=3, row=7, sticky=W)
        ttk.Button(mainframe, text='Borrar', command=partial(self.borrarEntrada)).grid(column=1, row=8, sticky=W)
        ttk.Button(mainframe, text='C', command=partial(self.borrarNumero)).grid(column=2, row=8, sticky=W)
        self.__panel.set('0')
        panelEntry.focus()
        self.__ventana.mainloop()
    def ponerNUMERO(self, numero):
        if self.__operadorAux==None:
            valor = self.__panel.get()
            self.__panel.set(valor+numero)
        else:
            self.__operadorAux=None
            valor=self.__panel.get()
            self.__primerOperando=valor
            self.__panel.set(numero)
    def borrarPanel(self):
        self.__panel.set('0')
    def resolverOperacion(self, operando1, operacion, operando2):
        resultado=0
        if operacion=='+':
            resultado=operando1+operando2
        else:
            if operacion=='-':
                resultado=operando1-operando2
            else:
                if operacion=='*':
                    resultado=operando1*operando2
                else:
                    if operacion=='/':
                        resultado=operando1/operando2
        self.__panel.set(str(resultado))
    def ponerOPERADOR(self, op):
        if op=='=':
            operacion=self.__operador.get()
            self.__segundoOperando=self.__panel.get()
            if isinstance(self.__primerOperandoImg,Imaginario) and type(self.__segundoOperando) != Imaginario:
                if self.__primerOperando == 'i':
                    self.__segundoOperandoImg = Imaginario(self.__segundoOperando,self.__primerOperando)
                else:
                    self.__segundoOperandoImg= Imaginario(self.__primerOperando,self.__segundoOperando)
            if (self.__primerOperando != 'i' or type(self.__primerOperandoImg) != Imaginario) and (self.__segundoOperando != 'i' or type(self.__segundoOperandoImg) != Imaginario):
                self.resolverOperacion(int(self.__primerOperando), operacion, int(self.__segundoOperando))
            if isinstance(self.__primerOperandoImg,Imaginario) and isinstance(self.__segundoOperandoImg,Imaginario):
                self.resolverOperacion(self.__primerOperandoImg, self.__operadorImg, self.__segundoOperandoImg)
            self.__operador.set('')
            self.__operadorAux=None
        else:
            if self.__operador.get()=='':
                self.__operador.set(op)
                self.__operadorAux=op
            else:
                operacion=self.__operador.get()
                self.__segundoOperando=self.__panel.get()
                if self.__primerOperando == 'i' or self.__segundoOperando == 'i':
                    if self.__primerOperando == 'i':
                        self.__primerOperandoImg = Imaginario(self.__segundoOperando,self.__primerOperando)
                    else:
                        self.__primerOperandoImg = Imaginario(self.__primerOperando,self.__segundoOperando)
                self.__operadorImg = op
                self.__operador.set('img {}'.format(op))
                self.borrarEntrada()
                self.__operadorAux=op
    def borrarEntrada(self):
        self.__panel.set(0)
    def borrarNumero(self):
        num = self.__panel.get()
        i = 0
        res = ''
        if(len(num) >= 2):
            while i < (len(num)-1):
                res += num[i]
                i+=1
            self.__panel.set(res)
        else:
            self.__panel.set(0)