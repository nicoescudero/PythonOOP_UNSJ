from classes.personal import Personal

class PersonalApoyo(Personal):
    def __init__(self,**kwargs):
        super().__init__(**kwargs)
        self.__categoria = kwargs['categoria']
    def __str__(self):
        return "%s \nCategoria: %s" % (super().__str__(), self.__categoria)
    def mostrarDatos(self):
        print("Agente Apoyo")
    def mostrarSueldo(self):
        antiguedad = (self.getSueldo()*(self.getAntiguedad()/5))/100
        sueldobasico = self.getSueldo()+antiguedad+(self.getSueldo()*0.10)
        print("Sueldo basico Agente Apoyo: ",sueldobasico)
    def getObjectType(self):
        return self.__class__.__name__
    def toJSON(self):
        d = dict(
            __class__=self.__class__.__name__,
            __atributos__=dict(
                cuil=self.getCuil(),
                apellido=super().getApellido(),
                nombre=self.getNombre(),
                sueldo=self.getSueldo(),
                antiguedad = self.getAntiguedad(),
                categoria = self.__categoria
            )
        )
        return d