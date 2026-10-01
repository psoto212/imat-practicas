#Problema 1
import math
import time
import matplotlib.pyplot as plt
"""
a)
"""
def Generarprimos(n)->list:
    i=2
    lista_primos=[]
    while len(lista_primos)<n:
        primo=True
        for j in range(2,i):
            if i%j==0:
                primo=False
        if primo:
            lista_primos.append(i)
        i+=1
    return lista_primos  
     
eje_x=[]
eje_y=[]
n=1
i=1
while n<1002:
    inicio=time.time()
    lista_primos=Generarprimos(n)
    fin=time.time()
    eje_y.append(fin-inicio)
    eje_x.append(i)
    n+=100
    i+=1
plt.plot(eje_x,eje_y, label="Primos")
plt.show()

"""
b)
"""
n=100
def Generarprimos_2(n)->list:
    i=2
    lista_primos=[]
    while len(lista_primos)<n:
        primo=True
        j=2
        while j<i and primo:
            if i%j==0:
                primo=False
            j+=1    
        if primo:
            lista_primos.append(i)
        i+=1
    return lista_primos   

eje_x=[]
eje_y=[]
n=1
i=1
while n<1002:
    inicio=time.time()
    lista_primos=Generarprimos_2(n)
    fin=time.time()
    eje_y.append(fin-inicio)
    eje_x.append(i)
    n+=100
    i+=1
plt.plot(eje_x,eje_y, label="Primos")
plt.show()        


"""
c)
"""
n=100
def Generarprimos_3(n)->list:
    i=3
    lista_primos=[2,3]
    while len(lista_primos)<n:
        primo=True
        j=3
        while j<i and primo:
            if i%j==0:
                primo=False
            
            j+=1    
        if primo:
            lista_primos.append(i)
        i+=2
    return lista_primos

eje_x=[]
eje_y=[]
n=1
i=1
while n<1002:
    inicio=time.time()
    lista_primos=Generarprimos_3(n)
    fin=time.time()
    eje_y.append(fin-inicio)
    eje_x.append(i)
    n+=100
    i+=1
plt.plot(eje_x,eje_y, label="Primos")
plt.show()


#Respuesta
def calcular_tiempo(funcion)->float:
    
    inicio=time.time()
    res=funcion
    fin=time.time()

    return fin-inicio


tiempo_1=calcular_tiempo(Generarprimos(n))
tiempo_2=calcular_tiempo(Generarprimos_2(n))
tiempo_3=calcular_tiempo(Generarprimos_3(n))

print(f"El tiempo de la primera funcion es :{tiempo_1:.12f}")
print(f"El tiempo de la segunda funcion es :{tiempo_2:.12f}")
print(f"El tiempo de la tercera funcion es :{tiempo_3:.12f}")