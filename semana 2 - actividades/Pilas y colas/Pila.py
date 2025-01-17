class Node:
    def __init__(self, valor):
        self.valor = valor
        self.next = None

class Pila:
    def __init__(self):
        self.last = None

    def push(self, valor):
        nodo = Node(valor)
        if self.last:
            nodo.next = self.last
        
        self.last = nodo

    def pop(self):
        if self.last:
            ultimo = self.last.valor
            self.last = self.last.next
            return ultimo
        print('ya no hay elementos en la pila')
        return None
    
pila = Pila()
numeros = [1,2,4,6,8,9,10]
for n in numeros:
    pila.push(n)

for i in range(7):
    print(pila.pop())