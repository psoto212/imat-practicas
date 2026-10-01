import time
import matplotlib.pyplot as plt
import random
def Esprimo(valor):
    if valor==1 or valor==2:
        return 1
    else:
        for i in range(2,valor):
            if valor%i==0:
                return 0
        return 1

def Separacion(vector,primos,no_primos):
    if len(vector)==0:
        return primos + no_primos
    else:    
       if Esprimo(vector[0])==1:
           primos.append(vector[0])
       else:
           no_primos.append(vector[0])
       return Separacion(vector[1:],primos,no_primos)
    
primos=[]
no_primos=[]
vector=[2,3,4,5,7,6,5,2,9,24,56]
s=Separacion(vector,primos,no_primos)
print(s)

"""
He decidido usar un algortimo recursivo para evitar el tiempo de mas que provocan los bucles
"""
eje_X=[]
eje_Y=[]
for i in range(1,100):
    eje_X.append(i)
    temp=0
    vector=[random.randint(1,20) for _ in range(1,100)]
    for j in range(10):
        inicio=time.time()
        s=Separacion(vector,primos,no_primos)
        fin=time.time()
        temp+=(inicio-fin)
    temp_medio=temp//10
    eje_Y.append(temp_medio)

plt.plot(eje_X,eje_Y)
plt.show()

"""
El orden es de =O(n**2)
Existen modelos mas eficientes si hubiesemos quizas prescindido de bucles en la funcion Esprimo, y si hubiesemos implementado la union de los numeros
primos con los no primos en el vector de otra manera y sin recurrir a otros 2 arrays, esto habria mejorado la eficiencia
"""