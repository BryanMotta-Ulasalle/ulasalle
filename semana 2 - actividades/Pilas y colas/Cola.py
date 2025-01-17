class Node:
    def __init__(self, valor):
        self.valor = valor
        self.next = None
    
class Cola:
    def __init__(self):
        self.first = None
        self.last = None
    def show(self):
        current = self.first
        while current != None:
            print(current.valor)
            current = current.next
            

    def encolar(self, valor):
        nodo = Node(valor)
        if self.last != None:
            self.first = nodo
            nodo.next = self.last
        self.last = nodo
    def getFirst(self):
        v = self.first.valor
        return v
    def getLast(self):
        v = self.last.valor
        return v
    def desencolar(self):
        if self.last == None:
            return str('no se puede')
        if self.first.next == None:
            ultimo = self.last
            self.first = None
            self.first = self.last
            return ultimo
        self.first = self.first.next

cola = Cola()
cola.encolar(1)
cola.encolar(2)
cola.encolar(3)
cola.encolar(4)
cola.show()
cola.getFirst()
cola.getLast()
cola.desencolar()
cola.show()
cola.desencolar()
cola.show()


