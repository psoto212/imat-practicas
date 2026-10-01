from threading import Semaphore, Thread
from time import sleep
import random



sem_lectores_mutex = Semaphore(1)
sem_escritores_mutex = Semaphore(1)
contador_lectores = 0
shared_x = 10

def lector(idx: int):
    global contador_lectores, shared_x
    for i in range(0, 10):
        sem_lectores_mutex.acquire()
        contador_lectores += 1
        if contador_lectores == 1:
            sem_escritores_mutex.acquire()
        sem_lectores_mutex.release()
        # Leemos el contenido
        print(f'Lector {idx} lee : {shared_x}' )

        sem_lectores_mutex.acquire()
        contador_lectores -= 1
        if contador_lectores == 0:
            sem_escritores_mutex.release()
        sem_lectores_mutex.release()
        sleep(random.uniform(0, 1))



def escritor(idx: int):
    global contador_lectores, shared_x
    for i in range(0, 10):
        sem_escritores_mutex.acquire()
        x = shared_x
        shared_x = random.uniform(10, 100)
        print(f'Escritor {idx} modifica : {x} a {shared_x}' )
        sem_escritores_mutex.release()
        sleep(random.uniform(0, 1))

if __name__ == '__main__':
    hilos = []
    for i in range(0, 1):
        escritor_t=Thread(target=escritor, args=(i,))
        escritor_t.start()
        hilos.append(escritor_t)
    
    for i in range(0, 3):
        lector_t=Thread(target=lector, args=(i,))
        lector_t.start()
        hilos.append(lector_t)

    for h in hilos:
        h.join()

   


