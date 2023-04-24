class email:
    __idCuenta = ''
    __dominio = ''
    __tipoDominio = ''
    __contraseña = ''
    #Item a
    def __init__(self,id,dominio,tipoDominio,contraseña):
        self.__idCuenta = id
        self.__dominio = dominio
        self.__tipoDominio = tipoDominio
        self.__contraseña = contraseña
    #Item b
    def retornaEmail(self):
        return self.__idCuenta + self.__dominio + self.__tipoDominio
    #Item c
    def getDominio(self):
        return self.__dominio
    #Item d
    def crearCuenta(self,address):
        idPart = address.split('@')
        domineParts = idPart[1].split('.')
        self.__idCuenta = idPart[0]
        self.__dominio = '@' + domineParts[0]
        self.__tipoDominio = '.' + domineParts[1]
        self.__contraseña = ''
        print('ACCOUNT Created...')
    #Function 1: Mensaje
    def sendMessage(self,name,address):
        return 'Estimado ' + name + ' te enviaremos tus mensajes a la dirección: ' + address
    #Function 2: Cambio de contraseña
    def setPassword(self,currentPassword, newPassword):
        if self.__contraseña == currentPassword:
            self.__contraseña == newPassword
            return 'SUCCESS... Contraseña cambiada'
        else:
            return 'ERROR: Las contraseñas no coinciden'