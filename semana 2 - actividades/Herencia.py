class Superclase:
    def __init__(self, nombre):
        self.nombre = nombre

class Subclase(Superclase):
    def __init__(self, nombre, apellido):
        super().__init__(nombre)
        self.__apellido = apellido
    def saludar(self):
        print('hola'+str(self.nombre)+str(self.__apellido))

persona = Subclase('bryan','Motta')
persona.saludar()