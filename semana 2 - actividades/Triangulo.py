class Triangulo:
    def __init__(self,base,altura):
        self.__base = base
        self.__altura = altura
    def get_base(self):
        return self.__base
    def set_base(self, base):
        self.__base = base
    def get_altura(self):
        return self.__altura
    def set_base(self, altura):
        self.__altura = altura
    def area(self):
        self.areaR = self.base *  self.altura

    def imprimirBase(self):
        print('la base es ' +str(self.base))
    def imprimirAltura(self):
        print('la altura es ' +str(self.altura))
    def imprimirArea(self):
        print('El area es '+str(self.areaR))
t = Triangulo(4,3)
t.area()
t.imprimirBase()
t.imprimirAltura()
t.imprimirArea()