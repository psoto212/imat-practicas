# Ejercicio1_Ap1_TuNombre.py

import time, random
from threading import Thread, Semaphore

BUFFER_SIZE = 10
buffer = [-1] * BUFFER_SIZE
in_idx = 0
out_idx = 0

mutex = Semaphore(1)
vacios = Semaphore(BUFFER_SIZE)
llenos = Semaphore(0)

ID_PRODUCTOR = 1
ID_CONSUMIDOR = 1

def productor(n_iter):
    global in_idx
    for _ in range(n_iter):
        vacios.acquire()
        mutex.acquire()
        try:
            if buffer[in_idx] == -1:
                valor = random.randint(1, 10)
                buffer[in_idx] = valor
                print(f"Productor {ID_PRODUCTOR}: ha producido: {valor}")
                in_idx = (in_idx + 1) % BUFFER_SIZE
        except:
            pass
        mutex.release()
        llenos.release()
        time.sleep(random.uniform(0, 1))

def consumidor(n_iter):
    global out_idx
    for _ in range(n_iter):
        llenos.acquire()
        mutex.acquire()
        try:
            if buffer[out_idx] != -1:
                valor = buffer[out_idx]
                buffer[out_idx] = -1
                print(f"Consumidor {ID_CONSUMIDOR}: ha leido: {valor}")
                out_idx = (out_idx + 1) % BUFFER_SIZE
        except:
            pass
        mutex.release()
        vacios.release()
        time.sleep(random.uniform(0, 1))

if __name__ == "__main__":
    iteraciones = 2 * BUFFER_SIZE
    t_prod = Thread(target=productor, args=(iteraciones,))
    t_cons = Thread(target=consumidor, args=(iteraciones,))
    t_prod.start()
    t_cons.start()
    t_prod.join()
    t_cons.join()
