class Nodo:
    def __init__(self, valor):
        self.valor = valor
        self.izquierdo = None
        self.derecho = None

class ArbolBinario:
    def __init__(self):
        self.raiz = None

    #Método para agregar de forma recursiva
    def agregar(self, valor):
        nuevo_nodo = Nodo(valor)
        if self.raiz is None:
            self.raiz = nuevo_nodo
        else:
            self._agregar_recursivo(self.raiz, nuevo_nodo)

    def _agregar_recursivo(self, nodo_actual, nuevo_nodo):
        if nuevo_nodo.valor < nodo_actual.valor:
            if nodo_actual.izquierdo is None:
                nodo_actual.izquierdo = nuevo_nodo
            else:
                self._agregar_recursivo(nodo_actual.izquierdo, nuevo_nodo)
        else:
            if nodo_actual.derecho is None:
                nodo_actual.derecho = nuevo_nodo
            else:
                self._agregar_recursivo(nodo_actual.derecho, nuevo_nodo)

    # Método para ordenar el arbol binario
    def inorden(self, nodo):
        if nodo is not None:
            self.inorden(nodo.izquierdo)
            print(nodo.valor, end=" ")
            self.inorden(nodo.derecho)
            
    # Método para buscar de forma recursiva

    def buscar(self, valor):
        return self._buscar_recursivo(self.raiz, valor)

    def _buscar_recursivo(self, nodo_actual, valor):
        if nodo_actual is None:
            return False
        if nodo_actual.valor == valor:
            return True
        elif valor < nodo_actual.valor:
            return self._buscar_recursivo(nodo_actual.izquierdo, valor)
        else:
            return self._buscar_recursivo(nodo_actual.derecho, valor)

    # Método para eliminar de forma recursiva
    def eliminar(self, valor):
        self.raiz = self._eliminar_recursivo(self.raiz, valor)

    def _eliminar_recursivo(self, nodo_actual, valor):
        if nodo_actual is None:
            return nodo_actual

        if valor < nodo_actual.valor:
            nodo_actual.izquierdo = self._eliminar_recursivo(nodo_actual.izquierdo, valor)
        elif valor > nodo_actual.valor:
            nodo_actual.derecho = self._eliminar_recursivo(nodo_actual.derecho, valor)
        else:
            # Nodo con solo un hijo o sin hijos
            if nodo_actual.izquierdo is None:
                return nodo_actual.derecho
            elif nodo_actual.derecho is None:
                return nodo_actual.izquierdo

            # Nodo con dos hijos: obtener el sucesor en inorden
            sucesor = self._minimo_valor(nodo_actual.derecho)
            nodo_actual.valor = sucesor.valor
            nodo_actual.derecho = self._eliminar_recursivo(nodo_actual.derecho, sucesor.valor)

        return nodo_actual

    def _minimo_valor(self, nodo):
        actual = nodo
        while actual.izquierdo is not None:
            actual = actual.izquierdo
        return actual

arbol = ArbolBinario()

# Agregar valores al árbol
valores = [50, 30, 70, 20, 40, 60, 80]
for v in valores:
    arbol.agregar(v)

print("\nRecorrido en inorden:")
arbol.inorden(arbol.raiz)

# Buscar valores en el árbol
print("\n\nBúsqueda de valores:")
for v in [40, 90]:
    encontrado = arbol.buscar(v)
    print(f"¿Está {v} en el árbol? {'Sí' if encontrado else 'No'}")

# Eliminar un valor del árbol
print("\nEliminando el valor 50 del árbol.")
arbol.eliminar(50)

print("Recorrido en inorden después de eliminar 50:")
arbol.inorden(arbol.raiz)
