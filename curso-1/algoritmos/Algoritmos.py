
#INSERCCION DIRECTA

import random

def inserccion_directa(vector):
    
    for j in range(1, len(vector)):
        clave = vector[j]
        i = j - 1

        while i >= 0 and vector[i] > clave:
            vector[i + 1] = vector[i]
            i = i - 1

        vector[i + 1] = clave
    
    return vector



#SELECTION SORT

def selection_sort(vector):
    
    for i in range(0,len(vector)-1):
        k=i
        clave=vector[i]

        for j in range(i+1, len(vector)):
            if vector[j]<clave:
                k=j
                clave=vector[j]

        vector[k]=vector[i]
        vector[i]=clave
        
    return vector


#BURBUJA

def bubble_sort(vector):
    
    for i in range(0,len(vector)):
        for j in range(0, len(vector)-i-1):
            if vector[j] > vector[j+1]:
                vector[j], vector[j+1] = vector[j+1], vector[j]
                
    return vector

#MEZCLA_DIRECTA


def merge_sort(vector):
    if len(vector) <= 1:
        return vector
    
    else:
        med = len(vector) // 2
        left = merge_sort(vector[:med])
        right = merge_sort(vector[med:])
        return merge(left, right)

def merge(left, right):
    merged = []
    while left and right:
        if left[0] < right[0]:
            merged.append(left.pop(0))
        else:
            merged.append(right.pop(0))
    
    merged.extend(left if left else right)
    return merged

#INSERCCION BINARIA

def inserccion_binaria(vector):
    for i in range(1, len(vector)):                                    
        current = vector[i]              # El elemento actual a insertar  
        left, right = 0, i - 1          # Encuentra la posición adecuada para insertar el elemento actual
        while left <= right:
            med = (left + right) // 2
            if vector[med] < current:
                left = med + 1
            else:
                right = med - 1
        for j in range(i, left, -1):       # Desplaza los elementos para hacer espacio para el elemento actual
            vector[j] = vector[j - 1]
        vector[left] = current               # Inserta el elemento actual en su posición adecuada
    return vector

#SACUDIDA

def sacudida_sort(vector):
    n = len(vector)
    start = 0
    end = n - 1
    while start < end:
        # Movemos el índice derecho hacia la izquierda
        for i in range(start, end):
            if vector[i] > vector[i + 1]:
                vector[i], vector[i + 1] = vector[i + 1], vector[i]
        
        # Decrementamos el índice derecho
        end -= 1
        
        # Movemos el índice izquierdo hacia la derecha
        for i in range(end - 1, start - 1, -1):
            if vector[i] > vector[i + 1]:
                vector[i], vector[i + 1] = vector[i + 1], vector[i]
        
        # Incrementamos el índice izquierdo
        start += 1
    
    return vector

#SHELL SORT

def shell_sort(vector):
    n = len(vector)
    med = n // 2
    while med > 0:
        for i in range(med, n):
            temp = vector[i]
            j = i
            while j >= med and vector[j - med] > temp:
                vector[j] = vector[j - med]
                j -= med
            vector[j] = temp
        med //= 2
        
    return vector

#QUICK SORT

def quick_sort(vector):
    if len(vector) <= 1:
        return vector
    else:
        pivote = vector[0]
        menores = [x for x in vector[1:] if x <= pivote]
        mayores = [x for x in vector[1:] if x > pivote]
        return quick_sort(menores) + [pivote] + quick_sort(mayores)



#BUCKET SORT

def bucket_sort(vector):
    
    maximo = max(vector)
    minimo = min(vector)
    rango_bucket = maximo - minimo + 1
    

    buckets = [[] for _ in range(rango_bucket)]
    
   
    for num in vector:
        buckets[num - minimo].append(num)
    
    vector_ordenado = []
    for bucket in buckets:
        vector_ordenado.extend(sorted(bucket))
    
    return vector_ordenado



#LECTOR CSV

import csv
from dataclasses import dataclass
import datetime
import time

# lets define a data class as a proxy for the record
@dataclass
class Trayecto:
    """Class for keeping track of an item in inventory."""
    date             : datetime.date         # fecha del viaje
    hour             : int                   # hora de inicio del viaje
    ageRange         : int                   # Rango de edad de los usuarios.
    user_type        : int                   # Tipo de Usuario.
    idumplug_station : int                   # Estación de origen.
    idplug_station   : int                   # Estación de destino.
    travel_time_secs : int                   # Tiempo del trayecto. (Secs)
    file_id          : str                   # Fichero.- Nombre del fichero de donde se ha obtenido la información.

    def __gt__(self, trayecto):
        # returns true if self is > other, by whatever criteria you want to  use
        raise NotImplementedError
    
    
def readTrayectos(iSize):
    sizes = [500,1000,5000,10000,500000,1000000]
    csvFile = f'bicimad_{sizes[iSize]}.csv'
    trayectos = []
    with open(csvFile) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=';')
        line_count = 0
        for row in csv_reader:
            if line_count == 0:
                line_count += 1
            else:
                try:
                    trayectos.append(int(row[6]))
                    line_count += 1
                except:
                    print (f"Badly formated row {row}")
        # print ( "Here are the first 10....")
        # for trayecto in trayectos[:10]: print (trayecto)
        return trayectos
    
