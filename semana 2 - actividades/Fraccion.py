class Fraccion:
    def crear(self,numerador,denominador):
        self.numerador = numerador
        self.denominador = denominador

    def valor(self):
        self.resultado = self.numerador / self.denominador
    
    def imprimir(self):
        print(self.resultado)
    
    def sumar(self, numerador2, denominador2):
        self.numerador2 = numerador2
        self.denominador2 = denominador2
        self.total = (self.numerador/self.denominador) + (self.numerador2/self.denominador2)
        print(self.total)

fraccion = Fraccion()
fraccion.crear(8,3)
fraccion.sumar(8,3)
#fraccion.valor()
#fraccion.imprimir()