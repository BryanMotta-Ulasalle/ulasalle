class Animal:
    def __init__(self):
        pass
    def hacer_sonido(self, sonido=None):
        print('los animales hacen sonidos')
class Vaca(Animal):
    def hacer_sonido(self):
        print('La vaca hace muu')
class Perro(Animal):
    def hacer_sonido(self):
        print('El perro ladra')
class Gato(Animal):
    def hacer_sonido(self):
        print('EL gato maulla')
        
perro = Perro()
gato = Gato()
vaca = Vaca()
animal = Animal()

animales=[perro, gato, vaca, animal, Gato()]
for ani in animales:
    ani.hacer_sonido()