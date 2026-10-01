import numpy as np
import random
from threading import Thread
import time





def escribir_matriz(numero_hilo, matriz_valores, contador_valores, repeticiones=20):
	for _ in range(repeticiones):
		fila_aleatoria = random.randint(0, len(matriz_valores) - 1)
		columna_aleatoria = random.randint(0,len(matriz_valores) - 1)
		matriz_valores[fila_aleatoria, columna_aleatoria] = numero_hilo

		if numero_hilo in contador_valores:
			contador_valores[numero_hilo] += 1

		else:
			contador_valores[numero_hilo] = 1


		time.sleep(1)


if __name__ == "__main__":

	try:
		cantidad_hilos = int(input("introduce el numero de hilos que desees: "))

	except:
		cantidad_hilos = 0

	if cantidad_hilos <= 0:
		print("numero de hilos introducidos no valido")


	else:
		n = 10
		matriz_valores = np.full((n,n), np.nan)
		contador_valores = {}

		lista_hilos = []


	for numero_hilo in range(1, cantidad_hilos +1):
		hilo = Thread(target = escribir_matriz, args = (numero_hilo, matriz_valores, contador_valores))
		lista_hilos.append(hilo)

		hilo.start()

	for hilo in lista_hilos:
		hilo.join()


	print("Matriz resultado")
	print(matriz_valores)

	conteo_en_matriz = {}
	for fila in matriz_valores:
		for valor in fila:
			if not np.isnan(valor):
				valor_int = int(valor)
				if valor_int in conteo_en_matriz:
					conteo_en_matriz[valor_int] += 1
				else:
					conteo_en_matriz[valor_int] = 1

	print(f"resultado: {conteo_en_matriz}")






"""
Al cambiar los hilos por procesos vemos que no corre el programa ya que como dice la teoría una de las grandes diferencias es que los hilos comparten su memoria entre ellos mientras que los
procesos no hacen tal cosa y cada accion que ejecutan se ve reflejada por lo que puede haber contradicciones entre ellos y por ello no correr el programa
"""

	
