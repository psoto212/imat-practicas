import matplotlib.pyplot as plt
import matplotlib.lines as lines
import datetime

class Nodo():
    def __init__(self,clave,valor):
        self.valor= valor
        self.clave=clave
        self.parent=None
        self.left=None
        self.right=None

class ArbolBinario():

    def __init__(self, raiz):
        self.raiz=raiz


    def mostrar(self):
        seq=self.secuenciar()
        print(seq)

    def secuenciar(self):
        seq=[]
        nodo=self.raiz

        if self.raiz:
            left=ArbolBinario(nodo.left)
            if left:
                seq+=left.secuenciar()
            seq.append(nodo.clave)

            right=ArbolBinario(nodo.right)
            if right:
                seq+=right.secuenciar()

        return seq

    def Buscarclave(self,clave):
        nodo=self.raiz
        if nodo != None:
            if clave < nodo.clave:
                left=ArbolBinario(nodo.left)
                return left.Buscarclave(clave)
            elif clave > nodo.clave:
                right=ArbolBinario(nodo.right)
                return right.Buscarclave(clave)
            else:
                return clave, nodo.valor
            
        else:
            return None
    def insertar(self, clave, valor):
        nuevo_nodo = Nodo(clave, valor)
        if self.raiz is None:
            self.raiz = nuevo_nodo
        else:
            self._insertar_recursivo(self.raiz, nuevo_nodo)


    def _insertar_recursivo(self, nodo_actual, nuevo_nodo):
        if nuevo_nodo.clave < nodo_actual.clave:
            if nodo_actual.left is None:
                nodo_actual.left = nuevo_nodo
                nuevo_nodo.parent = nodo_actual
            else:
                self._insertar_recursivo(nodo_actual.left, nuevo_nodo)
        elif nuevo_nodo.clave > nodo_actual.clave:
            if nodo_actual.right is None:
                nodo_actual.right = nuevo_nodo
                nuevo_nodo.parent = nodo_actual
            else:
                self._insertar_recursivo(nodo_actual.right, nuevo_nodo)
        else:
            print("La clave ya existe en el árbol.")

            
    def _borrar_nodo(self, nodo):
        if nodo.parent is None:  # Nodo es la raíz del árbol
            if nodo.left is None and nodo.right is None:  # Nodo es una hoja
                self.raiz = None
            elif nodo.left is None or nodo.right is None:  # Nodo tiene un hijo
                hijo = nodo.left if nodo.left else nodo.right
                hijo.parent = None
                self.raiz = hijo
            else:  # Nodo tiene dos hijos
                sucesor = self._encontrar_minimo(nodo.right)
                nodo.clave, nodo.valor = sucesor.clave, sucesor.valor
                self._borrar_nodo(sucesor)
        else:  # Nodo no es la raíz del árbol
            if nodo.left is None and nodo.right is None:  # Nodo es una hoja
                if nodo.parent.left == nodo:
                    nodo.parent.left = None
                else:
                    nodo.parent.right = None
            elif nodo.left is None or nodo.right is None:  # Nodo tiene un hijo
                hijo = nodo.left if nodo.left else nodo.right
                hijo.parent = nodo.parent
                if nodo.parent.left == nodo:
                    nodo.parent.left = hijo
                else:
                    nodo.parent.right = hijo
            else:  # Nodo tiene dos hijos
                sucesor = self._encontrar_minimo(nodo.right)
                nodo.clave, nodo.valor = sucesor.clave, sucesor.valor
                self._borrar_nodo(sucesor)
    def _encontrar_minimo(self, nodo):
        while nodo.left:
            nodo = nodo.left
        return nodo
    
    


N=Nodo(15 ,"Quince")
N1=Nodo(6,"seis")
N2=Nodo(18,"Dieciocho")
N11=Nodo(3,"tres")
N12=Nodo(7,"siete")
N111=Nodo(2,"dos")
N112=Nodo(4,"cuatro")
N122=Nodo(13,"trece")
N1221=Nodo(9,"nueve")
N21=Nodo(17,"Diecisiete")
N22=Nodo(20,"veinte")

N.left = N1
N.right = N2
N1.parent = N
N2.parent = N
N1.left = N11
N1.right = N12
N11.parent = N1
N12.parent = N1
N11.left = N111
N11.right = N112
N111.parent = N11
N112.parent = N11
N12.right = N122
N122.parent = N12
N122.left = N1221
N1221.parent = N122
N2.left = N21
N2.right = N22
N21.parent = N2
N22.parent = N2

Arbol = ArbolBinario(N)
clave=Arbol.Buscarclave(20)
print(clave)
Arbol.mostrar()
Arbol.insertar(21,"Veintiuno")
Arbol.insertar(2,"dos")
Arbol.insertar(16,"dieciseis")

Arbol.mostrar()
Arbol._borrar_nodo(N1221)
Arbol.mostrar()










