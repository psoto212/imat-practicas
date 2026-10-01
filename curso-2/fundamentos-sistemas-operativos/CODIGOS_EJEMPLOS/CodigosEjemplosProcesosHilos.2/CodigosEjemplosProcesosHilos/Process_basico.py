'''
from multiprocessing import Process
import time

def trabajo_proceso(idx: int):
    for i in range(0, 10):
        time.sleep(1)
        print(f"Soy el proceso {idx} y estoy en el segundo {i}")

if __name__ == "__main__":  
    proc1 = Process(target=trabajo_proceso, args=(0,))  
    proc1.start()

    proc2 = Process(target=trabajo_proceso, args=(1,))  
    proc2.start()

    proc1.join()
    proc2.join()
'''
## Con Pool

from multiprocessing import Pool
import time

def trabajo_proceso(idx: int):
    for i in range(0, 10):
        time.sleep(1)
        print(f"Soy el proceso {idx} y estoy en el segundo {i}")

if __name__ == "__main__":  
    idxs = [0, 1]
    p = Pool(2)
    p.map(trabajo_proceso, idxs)
