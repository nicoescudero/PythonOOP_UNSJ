import math
class PlanAhorro:
    def __init__(self,codigo=0,modelo='',version='',valor=0,cantidadCuotas=0,cuotasLicitar=0):
        self.__codigo = codigo
        self.__modelo = modelo
        self.__version = version
        self.__valor = valor
        self.__cantidadCuotas = cantidadCuotas
        self.__cuotasLicitar = cuotasLicitar

    def getCodigo(self): return self.__codigo
    def getModelo(self): return self.__modelo
    def getVersion(self): return self.__version
    def getValor(self): return self.__valor
    def getCantidadCuotas(self): return self.__cantidadCuotas
    def getCuotasLicitar(self): return self.__cuotasLicitar
    def getImporteCuota(self):
        return format((self.__valor/self.__cantidadCuotas)+self.__valor*0.10,'.2f')

    def setValor(self,value): self.__valor = value
    def setCuotasLicitar(self,value): self.__cuotasLicitar = value
    
    def licitacion(self): 
        importeCuota = (self.__valor/self.__cantidadCuotas)+self.__valor*0.10
        return format(self.__cuotasLicitar*importeCuota,'.2f')