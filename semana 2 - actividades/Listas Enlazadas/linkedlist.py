class Node:
    def __init__(self, dato):
        self.dato = dato
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def insert(self, dato):
        nodo = Node(dato)
        if not self.head:
            self.head = nodo
        else:
            actual=self.head
            while(actual.next != None):
                actual = actual.next
            actual.next = nodo
    def insertIni(self,dato):
        nodo = Node(dato)
        if not self.head:
            self.head = nodo
        else:
            actual=self.head
            while(actual.next != None):
                actual = actual.next
            nodo.next = self.head
            self.head = nodo
    def insert_orden(self,dato):
        nodo = Node(dato)
        if not self.head or self.head.dato < dato:
            
            nodo.next = self.head
            self.head = nodo
        actual = self.head
        while(actual.next and self.next.dato < dato):
            actual = actual.next
        nodo.next = actual.next
        actual.next = actual


    def show(self):
           actual = self.head
           while(actual != None):
               print(actual.dato)
               actual = actual.next
lista = LinkedList()
lista.insert_orden(10)
lista.insert_orden(1) 
lista.insert_orden(5)  

lista.show()
