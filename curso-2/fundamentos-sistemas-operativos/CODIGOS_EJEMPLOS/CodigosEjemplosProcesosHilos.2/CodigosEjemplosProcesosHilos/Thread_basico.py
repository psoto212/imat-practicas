'''
from threading import Thread
import time

def trabajo_hilo(idx: int):
    for i in range(0, 10):
        time.sleep(1)
        print(f"Soy el hilo {idx} y estoy en el segundo {i}")

if __name__ == "__main__":  
    proc1 = Thread(target=trabajo_hilo, args=(0,))  
    proc1.start()

    proc2 = Thread(target=trabajo_hilo, args=(1,))  
    proc2.start()

    proc1.join()
    proc2.join()
'''
# ThreadPool
from multiprocessing.pool import ThreadPool
import time

def trabajo_hilo(idx: int):
    for i in range(0, 10):
        time.sleep(1)
        print(f"Soy el hilo {idx} y estoy en el segundo {i}")

if __name__ == "__main__":  
    idxs = [0, 1]
    p = ThreadPool(2)
    p.map(trabajo_hilo, idxs)