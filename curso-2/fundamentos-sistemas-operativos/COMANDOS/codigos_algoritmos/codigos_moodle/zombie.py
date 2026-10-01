from multiprocessing import Process
import time
import sys

def level_1():
    print("I am the child and I finish")
    time.sleep(5)

if __name__ == '__main__':
    ps = []
    for i in range(10):
        process = Process(target=level_1)
        process.start()
        ps.append(process)
    time.sleep(20)
    for p in ps:
        p.join()