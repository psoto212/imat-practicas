from threading import Semaphore
from multiprocessing.pool import ThreadPool

# Con semaforos
mutex = Semaphore(1)
valor = 0
def funcion(iteracion: int):
    global valor
    for i in range(iteracion):
        mutex.acquire()
        c = valor
        valor = c + 1
        mutex.release()

if __name__ == '__main__':
    pool = ThreadPool(2)
    pool.map(funcion, [1000000, 1000000])
    pool.close()
    pool.join()

    print(f"Valor es {valor}")