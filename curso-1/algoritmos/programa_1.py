class Pila:
    def __init__(self, tamaño=None):
        self.items = [None] * tamaño
        self.tamaño = tamaño
        self.tope = -1

    def insertar(self, elemento):
        if self.tope < self.tamaño - 1:
            self.tope += 1
            self.items[self.tope] = elemento
        else:
            print("La pila está llena, no se puede insertar el elemento", elemento)

    def extraer(self):
        if self.tope >= 0:
            elemento = self.items[self.tope]
            self.items[self.tope] = None
            self.tope -= 1
            return elemento
        else:
            print("La pila está vacía, no se puede extraer ningún elemento")
            return None

    def mostrar(self):
        return print(self.items[:self.tope + 1])

pila = Pila(tamaño=5) 
pila.insertar(4)
pila.insertar(7)
pila.insertar(3)
pila.insertar(4)
pila.extraer()
pila.insertar(9)
pila.insertar(8)
pila.mostrar()



