class PlanController:
    def __init__(self,list):
        self.__list = list
    
    def actualizarValorVehiculo(self):
        for car in self.__list:
            print('\nCodigo: {}\tModelo: {}\tVersion: {}'.format(car.getCodigo(),car.getModelo(),car.getVersion()))
            value = int(input('Ingresar nuevo valor del vehiculo: \t'))
            car.setValor(value)
    
    def vehiculosDisponibles(self):
        value = float(input('\nIngresar valor:\t'))
        count = 0
        for car in self.__list:
            if(float(car.getImporteCuota()) <= value):
                print('Codigo: {}\tModelo: {}\tVersion: {}\tImporte Cuota: {}'.format(car.getCodigo(),car.getModelo(),car.getVersion(),car.getImporteCuota()))
                count+=1
        if count == 0: print('No se encontraron vehiculos')
    def monto_a_Pagar(self):
        for car in self.__list:
            print('Codigo: {}\tModelo: {}\tVersion: {}'.format(car.getCodigo(),car.getModelo(),car.getVersion()))
            print('Monto: ',car.licitacion())
    def modificar_Cantidad_Cuotas(self):
        plan = int(input('\nIngresar plan:\t'))
        i = 0
        found = False
        while i < len(self.__list):
            if(self.__list[i].getCodigo() == plan):
                print('Codigo: {}\tModelo: {}\tVersion: {}\tCuotas de licitacion: {}'.format(self.__list[i].getCodigo(),self.__list[i].getModelo(),self.__list[i].getVersion(),self.__list[i].getCuotasLicitar()))
                cantidad = int(input('\nIngresar nueva cantidad de cuotas de licitacion:\t'))
                self.__list[i].setCuotasLicitar(cantidad)
                found = True 
                i = len(self.__list)
            i+=1
        if found == False: print('\nPlan no encontrado...')
    
    def importeVehiculos(self):
        for car in self.__list:
            print('Codigo: {}\tModelo: {}\tVersion: {}\tValor: {}\tImporte de Cuota: {}'.format(car.getCodigo(),car.getModelo(),car.getVersion(),car.getValor(),car.getImporteCuota()))
