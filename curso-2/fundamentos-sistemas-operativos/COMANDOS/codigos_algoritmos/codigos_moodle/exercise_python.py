from multiprocessing import Process
import time
import sys
import os

def cre_p(procs: int):
    ps = []
    print(f"Soy {os.getpid()} y mi padre es {os.getppid()}")
    for i in range(0, procs):
        proc2 = Process(target=cre_p, args=(i - 1,))
        proc2.start()
        ps.append(proc2)

    for process in ps:
        process.join()

if __name__ == "__main__":  
    ps = []
    print(f"Soy {os.getpid()}")
    for i in range(4):
        if i % 2 == 0:
            proc2 = Process(target=cre_p, args=(2,))  
        else:
            proc2 = Process(target=cre_p, args=(1,))  
        ps.append(proc2)
        proc2.start()

    for process in ps:
        process.join()