from StackandQueue import Cola, Pilas
cola = Cola()
cola.enqueue(1)
cola.enqueue(2)
cola.enqueue(3)

print("Primer elemento de la cola:", cola.first())  # Debería mostrar 1
print("Tamaño de la cola:", cola.size())  # Debería mostrar 3

elemento = cola.dequeue()
print("Elemento eliminado de la cola:", elemento)  # Debería mostrar 1
print("Tamaño de la cola después de dequeue:", cola.size())  # Debería mostrar 2

pila = Pilas()
pila.push(1)
pila.push(2)
pila.push(3)

print("Tope de la pila:", pila.top())
print("Tamaño de la pila:", pila.size())
elemento = pila.pop()
print("Elemento eliminado de la pila:", elemento)

