from classes.personal import Personal

class Docente(Personal):
    def __init__(self,**kwargs):
        super().__init__(**kwargs)
        self.__carrera = kwargs['carrera']
        self.__cargo = kwargs['cargo']
        self.__catedra = kwargs['catedra']

    def __str__(self):
        return "%s \ncargo:%s \ncatedra:%s \ncarrera:%s" % (super().__str__(),self.__cargo,self.__catedra,self.__carrera)

    def getCarrera(self): return self.__carrera
    def getCargo(self): return self.__cargo
    def getCatedra(self): return self.__catedra

    def mostrarDatos(self):
        super().mostrarDatos()
        print("Agente Docente")

    def mostrarSueldo(self):
        antiguedad = (self.getSueldo() * ((self.getAntiguedad() / 5)*5)) / 100
        sueldobasico = self.getSueldo()+antiguedad
        if self.__cargo == "simple":
            sueldobasico+=self.getSueldo()+0.10
        elif self.__cargo == "semiexclusivo":
            sueldobasico += self.getSueldo() + 0.20
        elif self.__cargo == "exclusivo":
            sueldobasico += self.getSueldo() + 0.50
        print("Sueldo basico Agente Docente: ", sueldobasico)
    def getObjectType(self):
        return self.__class__.__name__
    def toJSON(self):
        d = dict(
            __class__=self.__class__.__name__,
            __atributos__=dict(
                cuil = super().getCuil(),
                apellido = super().getApellido(),
                nombre = super().getNombre(),
                sueldo = super().getSueldo(),
                antiguedad=super().getAntiguedad(),
                carrera = self.__carrera,
                cargo = self.__cargo,
                catedra = self.__catedra,
            )
        )
        return d