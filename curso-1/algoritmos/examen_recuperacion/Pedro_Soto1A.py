"""
ejercicio 1
"""
from cmath import inf
def BuscaSecuencia(A):
    n = len(A)
    if n == 0:
        return 0, None, None
    
    suma_minima = inf #iniciamos la suma en el infinito para asi asegurarnos que al menos el índice menor va a ser la secuencia mínima aunque no sea negativo
    suma_actual = 0
    inicio = 0
    inicio_sec = 0
    fin = 0
    
    for i in range(n):
        suma_actual += A[i]
        
        if suma_actual < suma_minima:
            suma_minima = suma_actual
            inicio = inicio_sec  #esto nos indica el inicio de la secuencia que buscamos
            fin = i
        
        if suma_actual > 0:
            suma_actual = 0
            inicio_sec = i + 1 
    
    valor_inicial = A[inicio] if inicio < n else None
    valor_final = A[fin] if fin < n else None
    
    return suma_minima, valor_inicial, valor_final

suma, valor_inicial, valor_final = BuscaSecuencia([1,2,-4,3,-6,4,5,6,7,8,9])
print("La suma mínima es:", suma)
print("El valor inicial es:", valor_inicial)
print("El valor final es:", valor_final)










"""
Ejercicio 2 crear el monticulo
"""

def heapfy(arr, n, i): #le agregamos a los valores su posicion izquierda o derecha dependiendo del padre que es el de mayor valor
    left=2*i+1
    right=2*i+2
    largest=i

    if left<n and arr[largest]<arr[left]:
        largest=left

    if right<n and arr[largest]<arr[right]:
        largest=right

    if largest != i:
        arr[i],arr[largest]=arr[largest],arr[i]
        heapfy(arr,n,largest)
    

def heapbuild(arr,n):

    for i in range (n//2-1,-1,-1):
        heapfy(arr,n,i)

    return arr

def heapsort(arr):
    n=len(arr)
    heapbuild(arr,n)

    for i in range(n-1,0,-1):
        arr[0],arr[i]=arr[i],arr[0]
        heapfy(arr,i,0)
    
    return arr



heapsort([27,31,46,12,97,37,55,78,25])

