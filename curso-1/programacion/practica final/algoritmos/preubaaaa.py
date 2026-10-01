def heapify(arr,n,i):
    left=2*i+1
    right=2*i+2
    largest=i
    if left<n and arr[largest]<arr[i]:
        largest=left
    if right<n and arr[largest]<arr[i]:
        largest=right
    if largest!=i:
        arr[i],arr[largest]=arr[largest],arr[i]
        heapify(arr,n,largest)

     
    
def heapbuild(arr,n):
    for i in range((n//2)-1,-1,-1):
        heapify(arr,n,i)

def heapsort(arr):
    n=len(arr)
    heapbuild(arr,n)
    for i in range(n-1,0,-1):
        arr[0],arr[i],=arr[i],arr[0]
        heapify(arr,i,0)
    return arr

arr=[2,1,4,5,6,7,3]
vector=heapsort(arr)


class Nodo():
    def __init__(self,clave):
        self.clave=clave
        self.left=None
        self.right=None
        self.parent=None

class Mont():
    def __init__(self,aRootNode:Nodo):
        self.raiz=aRootNode

    def Construir_arbol(self,arr,i):
        raiz=Nodo(arr[i])
        if len(arr)==0:
            return 
        else:
            Nodo_hijo_left=2*i+1
            Nodo_hijo_right=2*i+2
            raiz.left=Nodo_hijo_left
            raiz.right=Nodo_hijo_right
            Nodo_hijo_left.parent=raiz
            Nodo_hijo_right.parent=raiz
            return self.Construir_arbol(arr,i+1)
   
    def addChildren(self,node: Nodo, index, arr):
        left_index = 2* index + 1
        right_index = 2*index + 2
        if left_index < len(arr):
            lChild = Nodo(arr[left_index])
            node.left = lChild
            lChild.parent = node
            self.addChildren(lChild, left_index, arr)
        if right_index < len (arr) :
            rChild = Nodo(arr[right_index])
            node. right = rChild
            rChild.parent = node
            self.addChildren(rChild, right_index, arr)
    rNode = Nodo(arr[0])



Raiz=Nodo(arr[0])
Monticulo=Mont(Raiz)
Monticulo.Construir_arbol(vector,0)
Monticulo.Secuenciar()


