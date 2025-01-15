class Figura:
    def area(self, a=None, b=None):
        print('se puede hallar el area de la figura geometrica')
class Cuadrado(Figura):
    def area(self, lado, altura=None):
        res=lado * altura
        print('el area del cuadrado es: '+str(res))
class Rectangulo(Figura):
    def area(self, lado, altura):
        res=lado * altura
        print('el area del rectangulo es: '+str(res))
cuadrado = Cuadrado()
rectangulo = Rectangulo()
figura = Figura()

lista=[cuadrado, rectangulo, figura]
for ani in lista:
    ani.area(2,2)
