class Triangulo:
    def __init__(self,base,altura):
        self.base = base
        self.altura = altura
    
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