from classes.personal import Personal

class Investigador(Personal):
    def __init__(self,**kwargs):
        super().__init__(**kwargs)
        self.__area = kwargs['area']
        self.__tipo = kwargs['tipo']
    def __str__(self):
        return "%s \narea:%s \ntipo:%s" % (super().__str__(),self.__area,self.__tipo)
    def getArea(self): return self.__area
    def getTipo(self): return self.__tipo
    def mostrarDatos(self):
        print("Agente Investigador")
    def mostrarSueldo(self):
        antiguedad = (self.getSueldo() * ((self.getAntiguedad() / 5)*5)) / 100
        sueldobasico = antiguedad + self.getSueldo()
        print("Sueldo Total del agente Investigador: ", sueldobasico)
    def getObjectType(self):
        return self.__class__.__name__
    def toJSON(self):
        d = dict(
            __class__=self.__class__.__name__,
            __atributos__=dict(
                cuil = self.getCuil(),
                apellido = self.getApellido(),
                nombre = self.getNombre(),
                sueldo = self.getSueldo(),
                antiguedad=self.getAntiguedad(),
                area = self.__area,
                tipo = self.__tipo
            )
        )
        return d