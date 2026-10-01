from threading import Thread, Event
import time
seguir_escribiendo = True
tiempo_acabado= [False]
def contador():
	segundos = 20
	while segundos > 0 and seguir_escribiendo:
		print(f"le quedan {segundos} segundos")
		time.sleep(5)
		segundos -= 5
	if seguir_escribiendo:
		print("no se ha introducido ningun nombre")
		tiempo_acabado[0] = True

if __name__ == "__main__":

	hilo = Thread(target=contador)
	hilo.start()
	nombre = ""
	while not nombre.strip():
		nombre=input("introduce tu nombre: ")

	apellido = ""
	while not apellido.strip():
		apellido=input("introduce tu/s apellidos: ")

	seguir_escribiendo = False
	hilo.join()
	if tiempo_acabado[0]:
		print(f"Ha ntroducido el nombre demasiado tarde")
	else:
		print(f"Bienvenido/a {nombre} {apellido}")

