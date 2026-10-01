import random
import time
import matplotlib.pyplot as plt


def heapfy(arr, n, i):
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


eje_x=[]
eje_y=[]
j=0

for i in range(10,10000,100):
    tiempo_medio=0
    for j in range(10):
        arr=[random.randint(1,200) for i in range(1,i)]

        t0=time.time()
        sort_list=heapsort(arr)
        t1=time.time()
        tiempo=t1 - t0
        tiempo_medio+=tiempo


    eje_x.append(i)
    eje_y.append(tiempo_medio/10)
    
    j+=1


plt.plot(eje_x,eje_y)
plt.show()



### Implementacion Cola Prioridad