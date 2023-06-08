from classes.personal import Personal
from classes.docente import Docente
from classes.investigador import Investigador

class DocenteInvestigador(Docente,Investigador):
    __categoria = 0
    __importeextradocencia = 0
    __importeextrainvestigador = 0

    def __init__(self,**kwargs):
        super().__init__(**kwargs)
        self.__categoria = int(kwargs['categoria'])
        self.__importeextradocencia = int(kwargs['importeextradocencia'])
        self.__importeextrainvestigador = int(kwargs['importeextrainvestigador'])

    def __str__(self):
        return "%s \nCategoria:%s \nImporte Extra Docencia: %s \nImporte Extra Investigador: %s" % (super().__str__(),self.__categoria, self.__importeextradocencia,self.__importeextrainvestigador)
    def getCategoria(self):
        return self.__categoria
    def getImporteExtradocencia(self):
        return self.__importeextradocencia
    def getImporteExtraInvestigador(self):
        return self.__importeextrainvestigador
    def mostrarDatos(self):
        print('{} {} Cuil: {}'.format(self.getApellido(),self.getNombre(),self.getCuil()))
        print('Antiguedad: {} Sueldo: ${}'.format(self.getAntiguedad(),self.getSueldo()))
        print('Area: {} Tipo: {}'.format(self.getArea(), self.getTipo()))
        print('Carrera: {} Cargo: {} Catedra: {}'.format(self.getCarrera(),self.getCargo(),self.getCatedra()))
        print('Categoria: {}'.format(self.__categoria))
        print('Importe extra Docencia: {}'.format(self.__importeextradocencia))
        print('Importe extra Investigador: {}'.format(self.__importeextrainvestigador))
    def mostrarSueldo(self):
        print("Sueldo Total del agente Docente-Investigador: ", super().mostrarSueldo())    
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
                area = self.getArea(),
                tipo = self.getTipo(),
                cargo = self.getCargo(),
                catedra = self.getCatedra(),
                carrera = self.getCarrera(),
                antiguedad = self.getAntiguedad(),
                categoria = self.__categoria,
                importeextradocencia = self.__importeextradocencia,
                importeextrainvestigador = self.__importeextrainvestigador
            )
        )
        return d