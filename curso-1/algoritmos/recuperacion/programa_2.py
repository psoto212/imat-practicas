class Cola():
 
    def __init__(self, tamaño=None):
       self.items=[None]*(tamaño+1)
       self.tamaño=tamaño+1
       self.head=0
       self.tail=0
   
    def insertar(self, item):
        if (self.tail+1)%self.tamaño==self.head:
           print("La cola está llena, no se puede agregar más elementos.")
 
        else:
            print("self.tail después de insertar:", self.tail)
            self.items[self.tail] = item
            self.tail = (self.tail + 1) % self.tamaño
       
    def extraer(self):
        if self.head == self.tail:
            print("La cola está vacía, no se puede extraer ningún elemento.")
            return None
        else:
            elemento = self.items[self.head]
            self.head = (self.head + 1) % self.tamaño
            return elemento
       
    def show(self):
        print("Elementos en la cola (FIFO):")
        if self.head <= self.tail:
            print(self.items[self.head:(self.tail)])
        else:
            print(self.items[self.head:] + self.items[:self.tail])
 
 
 
lista=Cola(6)
lista.insertar(2)
lista.insertar(4)
lista.insertar(8)
lista.insertar(7)
lista.insertar(1)
lista.insertar(3)
lista.extraer()
lista.extraer()
lista.insertar(8)
lista.extraer()
lista.show()


print(3%3)