# Codigo para los procesos con Process

from multiprocessing import Process
import time
import os

variable_global = 5


def f1(segundos):
    time.sleep(segundos)
    print(f"Finalizada la tarea en {segundos} realizada por el proceso {os.getpid()}")
    global variable_global

    variable_global += 10
    print(f"La variable tiene un valor de {variable_global}")


def f2(segundos):
    time.sleep(segundos)
    print(f"Finalizada la tarea en {segundos}")
    global variable_global
    variable_global += 5
    print(f"Finalizada la tarea en {segundos} realizada por el proceso {os.getpid()}")


if __name__ == '__main__':
    procs = []
    p1 = Process(target=f1, args=(5,))
    p1.start()
    procs.append(p1)
    p2 = Process(target=f2, args=(3,))
    p2.start()
    procs.append(p2)

    for p in procs:
        p.join()



'''
# Codigo para los procesos con Pool
from multiprocessing import Pool
import os
import time

trabajos = (["1", 5], ["2", 3], ["3", 1], ["4", 2])


def tarea(trabajos):
    id_trabajo = trabajos[0]
    segundos_espera = trabajos[1]
    print(f"Tarea {id_trabajo} siendo realizada por el proceso {os.getpid()}. Esperando {segundos_espera}")
    time.sleep(segundos_espera)
    print(f"Tarea {id_trabajo} Terminado.")


if __name__ == '__main__':
    p = Pool(2)
    p.map(tarea, trabajos)
'''

'''
# Hilos ejemplo 1
from threading import Thread
import time
import os

variable_global = 5


def f1(segundos):
    time.sleep(segundos)
    print(f"Finalizada la tarea en {segundos} realizada por el proceso {os.getpid()}")
    global variable_global

    variable_global += 10
    print(f"La variable tiene un valor de {variable_global}")


def f2(segundos):
    time.sleep(segundos)
    print(f"Finalizada la tarea en {segundos} realizada por el proceso {os.getpid()}")
    global variable_global
    variable_global += 5
    print(f"La variable tiene un valor de {variable_global}")


if __name__ == '__main__':
    threads = []
    th1 = Thread(target=f1, args=(5,))
    th1.start()
    threads.append(th1)
    th2 = Thread(target=f2, args=(3,))
    th2.start()
    threads.append(th2)

    for th in threads:
        th.join()
'''

# Codigo para los hilos con Pool
from multiprocessing.pool import ThreadPool
import threading
import os
import time

trabajos = (["1", 5], ["2", 3], ["3", 1], ["4", 2])


def tarea(trabajos):
    id_trabajo = trabajos[0]
    segundos_espera = trabajos[1]
    print(f"Tarea {id_trabajo} siendo realizada por el proceso {os.getpid()} (id del hilo {threading.get_ident()}). Esperando {segundos_espera}")
    time.sleep(segundos_espera)
    print(f"Tarea {id_trabajo} Terminado.")


if __name__ == '__main__':
    p = ThreadPool(2)
    p.map(tarea, trabajos)