class Equipo:
    def __init__(self, nombre=None, estadio=None, capacidad_estadio=None, num_ligas=0, num_copas_europa=0):
        self.nombre = nombre
        self.estadio = estadio
        self.capacidad_estadio = capacidad_estadio
        self.num_ligas = num_ligas
        self.num_copas_europa = num_copas_europa
        self.next = None
        self.prev = None

    def __str__(self):
        return (f'\nEl nombre del equipo es: {self.nombre}' +
                f'\nEl nombre del Estadio es: {self.estadio}' +
                f'\nLa capacidad del Estadio es: {self.capacidad_estadio}' +
                f'\nEl número de Ligas es: {self.num_ligas}' +
                f'\nEl número de Copas de Europa es: {self.num_copas_europa}')


class ListaEnlazada:
    def __init__(self):
        self.head = None
        self.tail = None
        self.current = None

    def AnadirNodo(self, nodo=Equipo()):
        if self.head is None:
            self.head = nodo
            self.tail = nodo
            self.current = nodo
        else:
            nodo.prev = self.tail
            self.tail.next = nodo
            self.tail = nodo

    def MostrarLista(self):
        actual = self.head
        while actual:
            print(f"{actual.nombre}", end=" -> ")
            actual = actual.next

    def Avanzar(self):
        if self.current.next:
            self.current = self.current.next
        else:
            print("Ya estás en la última posición.")
            self.MostrarUltimo()

    def Retroceder(self):
        if self.current.prev:
            self.current = self.current.prev
        else:
            print("Ya estás en la primera posición.")
            self.MostrarPrimero()

    def MostrarUltimo(self):
        print("\nÚltimo nodo:")
        print(self.tail)

    def MostrarPrimero(self):
        print("\nPrimer nodo:")
        print(self.head)


def Menu():
    print("\nMENU")
    print("1. Insertar un nuevo equipo")
    print("2. Avanzar por la lista")
    print("3. Retroceder por la lista")
    print("4. Mostrar todos los Equipos del Sistema")
    print("5. Salir")
    opc = int(input("Introduzca una opción: "))
    return opc


if __name__ == "__main__":
    lista = ListaEnlazada()
    opc = Menu()
    while opc != 5:
        if opc == 1:
            nombre = input("Ingrese el nombre del equipo: ")
            estadio = input("Ingrese el nombre del estadio: ")
            capacidad = input("Ingrese la capacidad del estadio: ")
            ligas = input("Ingrese el número de Ligas: ")
            copas = input("Ingrese el número de Copas de Europa: ")
            nuevo_equipo = Equipo(nombre, estadio, capacidad, ligas, copas)
            lista.AnadirNodo(nuevo_equipo)
        elif opc == 2:
            lista.Avanzar()
        elif opc == 3:
            lista.Retroceder()
        elif opc == 4:
            print("\nEquipos en la lista:")
            lista.MostrarLista()
            print()
        opc = Menu()

