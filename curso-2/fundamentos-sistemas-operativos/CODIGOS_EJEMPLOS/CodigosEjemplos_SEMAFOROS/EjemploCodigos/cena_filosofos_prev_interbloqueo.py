from threading import Semaphore
from multiprocessing.pool import ThreadPool
import random, time

FILOSOFOS = 5
tenedores = [Semaphore(1) for i in range(FILOSOFOS)]

def izquierda(i): 
    return (i + 1) % FILOSOFOS

def derecha(i):
    return i

def coge_tenedores(i):
    tenedores[izquierda(i)].acquire()
    time.sleep(1)
    tenedores[derecha(i)].acquire()

def deja_tenedores(i):
    tenedores[izquierda(i)].release()
    tenedores[derecha(i)].release()

def filosofo(i : int):
    while True:
        #Pensar
        print(f'Filosofo {i} piensa')
        time.sleep(random.uniform(0, 1))
        coge_tenedores(i)
        #Comer
        print(f'Filosofo {i} come')
        time.sleep(random.uniform(0, 1))
        deja_tenedores(i)

if __name__ == '__main__':
    pool = ThreadPool(FILOSOFOS)
    pool.map(filosofo, [i for i in range(FILOSOFOS)])
    pool.close()
    pool.join()
