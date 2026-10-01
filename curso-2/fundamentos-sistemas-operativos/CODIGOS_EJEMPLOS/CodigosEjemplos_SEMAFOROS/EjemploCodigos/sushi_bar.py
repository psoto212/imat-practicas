from threading import Semaphore, Thread
import time
import random

mutex = Semaphore(1)
bloqueado = Semaphore(0)
esperando, comiendo = 0, 0


def cliente(idx: int):
    global esperando, comiendo
    mutex.acquire()
    if comiendo == 5:
        esperando += 1 # Toca esperar
        print(f'Hilo {idx}, estoy esperando')
        mutex.release()
        bloqueado.acquire()
    else:
        comiendo += 1
        mutex.release()

    print(f'Hilo {idx}, voy a comer')
    time.sleep(random.uniform(5, 10)) # Comemos

    mutex.acquire()
    comiendo -= 1
    if comiendo == 0:
        tanda = min(esperando, 5)
        esperando -= tanda
        comiendo += tanda
        if tanda > 0:
            bloqueado.release(tanda)
    mutex.release()


if __name__ == '__main__':
    
    hilos = []
    for i in range(0, 20):
        cliente_th = Thread(target=cliente, args=(i,))
        cliente_th.start()
        hilos.append(cliente_th)


    for h in hilos:
        h.join()    