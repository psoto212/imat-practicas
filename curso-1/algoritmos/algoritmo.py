"""
a)El numero maximo de singulares posibles es N puesto que como 
los elementos del vector se pueden repetir existe la posibilidad de que dichos 
elementos fuesen todos el mismo de manera que todos los elementos serian singulares
ya que si por ejemplo el elemento repetido N veces es 2 en la cuarta posicion tendriamos
2+2+2+2/4 = 2 y asi en todo el vector al ser estas sumas el resultasdo de multiplicar 2 por la posicion en la encontremos
y al dividir para hallar el singular estaremos dividiendo por este indicador de posicion siendo siempre el resultado 2
"""
from time import perf_counter as pt
import random
import numpy as np

def MINsingularINGENUO(A):  
  indices=[]
  valor=A[0]
  inicio=pt()
  for i in range(1,len(A)-1):
      valor+=A[i]
      resul=valor/(i+1)
      if resul==A[i+1]:
          indices.append(i+1)
  fin=pt()
  tiempo_ejec=(fin-inicio)
  return indices,tiempo_ejec

tamaño=50000
vueltas=0
eje_x=[]
eje_y=[]
tiempo_total=0
Valor_MAx=200000

while tamaño<Valor_MAx:
   A=[]
   for i in range(tamaño):
           A.append(random.randint(1,10))
   tiempo_int=[]
   rep=0
   while rep<5:
       
         indices,tiempo_ejec=MINsingularINGENUO(A)
         tiempo_int.append(tiempo_ejec)
         rep+=1
   tiempo_medio=np.mean(tiempo_int)
   print(f"Con un vector de {tamaño}, el tiempo medio de ejecucion fue de {tiempo_medio:.9f} nanosegundos")
   eje_x.append(vueltas)
   eje_y.append(tiempo_medio)
   tamaño+=50000
   tiempo_total+=tiempo_ejec
   vueltas+=1

print(f"El tiempo medio de ejecucion fue {tiempo_total/vueltas}")

import matplotlib.pyplot as plt

plt.plot(eje_x,eje_y, label="Eficiencia")
plt.title("Eficiencia algoritmos")
plt.legend()
plt.show()