class Equipo:
    def __init__(self, nombre=None, estadio=None, capacidad_estadio=None, num_ligas=0, num_copas_europa=0):
        self.nombre = nombre
        self.estadio = estadio
        self.capacidad_estadio = capacidad_estadio
        self.num_ligas = num_ligas
        self.num_copas_europa = num_copas_europa
        self.next = None

    def __str__(self):
        return (f'\nEl nombre del equipo es: {self.nombre}' +
                f'\nEl nombre del Estadio es: {self.estadio}' +
                f'\nLa capacidad del Estadio es: {self.capacidad_estadio}' +
                f'\nEl número de Ligas es: {self.num_ligas}' +
                f'\nEl número de Copas de Europa es: {self.num_copas_europa}')

    def getSiguiente(self):
        return self.next
    
    def setSiguiente(self, next):
        self.next = next
 
    def getNombre(self):
        return self.nombre

    def setNombre(self, nombre):
        self.nombre = nombre

    def getEstadio(self):
        return self.estadio

    def setEstadio(self, estadio):
        self.estadio = estadio

    def getCapacidadEstadio(self):
        return self.capacidad_estadio

    def setCapacidadEstadio(self, capacidad_estadio):
        self.capacidad_estadio = capacidad_estadio

    def getNumLigas(self):
        return self.num_ligas

    def setNumLigas(self, num_ligas):
        self.num_ligas = num_ligas

    def getNumCopasEuropa(self):
        return self.num_copas_europa

    def setNumCopasEuropa(self, num_copas_europa):
        self.num_copas_europa = num_copas_europa


class ListaEnlazada:
    def __init__(self):
        self.head = None

    def AnadirNodo(self, nodo=Equipo()):
        if self.head is None:
            self.head = nodo
        else:
            actual = self.head
            while actual.next:
                actual = actual.next
            actual.next = nodo

    def MostrarLista(self):
        actual = self.head
        while actual:
            print(f"{actual.nombre}", end=" -> ")
            actual = actual.next

    def BuscarNodo(self, nombre):
        actual = self.head
        while actual:
            if actual.nombre == nombre:
                return actual
            actual = actual.next
        return None

    def BorrarNodo(self, nombre):
        actual = self.head
        previo = None
        while actual and actual.nombre != nombre:
            previo = actual
            actual = actual.next
        if previo is None:
            self.head = actual.next
        elif actual:
            previo.next = actual.next
            actual.next = None  # Elimina la referencia del nodo eliminado        
   
    def BorrarLista(self):
        self.head = None

    def ActualizarNodo(self, nombre):
        nodo = self.BuscarNodo(nombre)
        if nodo:
            # Modifica el nodo con nuevos datos
            nuevo_nombre = input("Ingrese el nuevo nombre del equipo: ")
            nodo.setNombre(nuevo_nombre)
            nuevo_estadio = input("Ingrese el nuevo estadio del equipo: ")
            nodo.setEstadio(nuevo_estadio)
            nueva_capacidad = input("Ingrese la nueva capacidad del estadio: ")
            nodo.setCapacidadEstadio(nueva_capacidad)
            nuevos_ligas = input("Ingrese el nuevo número de Ligas: ")
            nodo.setNumLigas(nuevos_ligas)
            nuevas_copas = input("Ingrese el nuevo número de Copas de Europa: ")
            nodo.setNumCopasEuropa(nuevas_copas)
            print("Equipo actualizado correctamente.")
        else:
            print("El equipo no se encuentra en la lista.")

def Menu():
    print("MENU")
    print("1. Insertar un nuevo equipo")
    print("2. Borrar un equipo")
    print("3. Buscar equipo por nombre")
    print("4. Listar todos los Equipos del Sistema")
    print("5. Actualizar nodo")
    print("6. Borrar toda la lista enlazada")
    print("7. Salir")
    opc = int(input("Introduzca una opcion: "))
    return opc

if __name__ == "__main__":
    lista = ListaEnlazada()
    opc = Menu()
    while opc != 7:
        if opc == 1:
            nombre = input("Ingrese el nombre del equipo: ")
            estadio = input("Ingrese el nombre del estadio: ")
            capacidad = input("Ingrese la capacidad del estadio: ")
            ligas = input("Ingrese el número de Ligas: ")
            copas = input("Ingrese el número de Copas de Europa: ")
            nuevo_equipo = Equipo(nombre, estadio, capacidad, ligas, copas)
            print(nuevo_equipo)
            lista.AnadirNodo(nuevo_equipo)
        elif opc == 2:
            nombre = input("Ingrese el nombre del equipo a borrar: ")
            lista.BorrarNodo(nombre)
        elif opc == 3:
            nombre = input("Ingrese el nombre del equipo a buscar: ")
            equipo = lista.BuscarNodo(nombre)
            if equipo:
                print("Información del equipo encontrado:")
                print(equipo)
            else:
                print("El equipo no se encuentra en la lista.")
        elif opc == 4:
            print("Equipos en la lista:")
            lista.MostrarLista()
            print()
        elif opc == 5:
            nombre = input("Ingrese el nombre del equipo a actualizar: ")
            lista.ActualizarNodo(nombre)
        elif opc == 6:
            lista.BorrarLista()
            print("Lista enlazada borrada correctamente.")
        opc = Menu()
