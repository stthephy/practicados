class Nodo:
    def __init__(self, dato):
        self.dato = dato
        self.siguiente = None

class Pilas:
    def __init__(self):
        self.head = None

    def push(self, item):
        nuevo_nodo = Nodo(item)
        nuevo_nodo.siguiente = self.head
        self.head = nuevo_nodo

    def pop(self):
        if not self.is_empty():
            dato = self.head.dato
            self.head = self.head.siguiente
            return dato
        else:
            return "La pila está vacía"

    def top(self):
        if not self.is_empty():
            return self.head.dato
        else:
            return "La pila está vacía"

    def is_empty(self):
        return self.head is None

    def size(self):
        contador = 0
        actual = self.head
        while actual:
            contador += 1
            actual = actual.siguiente
        return contador

class Cola:
    def __init__(self):
        self.frente = None
        self.final = None

    def enqueue(self, item):
        nuevo_nodo = Nodo(item)
        if self.is_empty():
            self.frente = nuevo_nodo
            self.final = nuevo_nodo
        else:
            self.final.siguiente = nuevo_nodo
            self.final = nuevo_nodo

    def dequeue(self):
        if not self.is_empty():
            dato = self.frente.dato
            self.frente = self.frente.siguiente
            if self.frente is None:
                self.final = None
            return dato
        else:
            return "La cola está vacía"

    def first(self):
        if not self.is_empty():
            return self.frente.dato
        else:
            return "La cola está vacía"

    def is_empty(self):
        return self.frente is None

    def size(self):
        contador = 0
        actual = self.frente
        while actual:
            contador += 1
            actual = actual.siguiente
        return contador

