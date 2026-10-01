from multiprocessing import Process
import time
import os

def bucle(i):
	print(f"soy el hijo{i+1} con id: {os.getpid()} y mi padre tiene id {os.getppid()}.")

	while True:

        	pass



def configuracion_1():
	procesos = []
	print("creando 3 procesos hijo")

	for i in range(3):
		proceso = Process(target = bucle, args=(i,), name = f"hijo{i+1}")
		procesos.append(proceso)
		proceso.start()
	time.sleep(15)
	for numero_proceso,  p in enumerate(procesos, start = 1):
		print("eliminando los procesos hijo")
		p.terminate()
		
		p.join()
		if numero_proceso < len(procesos): 
			time.sleep(5)

		print("procesos hijo eliminados")





def crear_hijo_en_cadena(nivel):
    print(f"Soy el proceso de nivel {nivel} con id {os.getpid()} y mi padre tiene id {os.getppid()}.")
    if nivel < 3:
        hijo = Process(target=crear_hijo_en_cadena, args=(nivel + 1,), name=f"hijo_nivel_{nivel+1}")
        hijo.start()
    while True:
        pass



def configuracion_2():
    procesos = []
    primer_hijo = Process(target=crear_hijo_en_cadena, args=(1,), name="hijo_nivel_1")
    procesos.append(primer_hijo)
    primer_hijo.start()
    time.sleep(15)
    primer_hijo.terminate()
    primer_hijo.join()




if __name__ == "__main__":

	eleccion = int(input("diga un numero entre 1 y 2: "))
	if eleccion == 1:
		configuracion_1()


	elif eleccion == 2:
		configuracion_2()

	else:
		print("El proceso ha terminado")











"""
Configuración 1:
El proceso principal crea tres hijos y, después de 15 segundos, los va matando uno a uno cada 5 segundos.
Todos terminan bien porque el padre controla su cierre con terminate() y join(), así que no quedan procesos zombis ni huérfanos.

Configuración 2:
El proceso principal crea un hijo que crea otro y así hasta tres niveles.
Tras 15 segundos, el padre solo mata al primer hijo, pero los demás siguen vivos y se vuelven procesos huérfanos.
Esto pasa porque su padre muere antes que ellos, aunque el sistema los mantiene activos.





"""
