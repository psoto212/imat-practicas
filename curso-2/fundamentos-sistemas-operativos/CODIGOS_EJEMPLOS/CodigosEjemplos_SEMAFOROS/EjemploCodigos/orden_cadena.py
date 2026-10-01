from threading import Semaphore, Thread
import time as t
a = Semaphore(1)
b = Semaphore(0)
c = Semaphore(0)

def hilo1():
    global a, b
    while True:
        a.acquire()
        print(f'H')
        print(f'E')
        b.release()
        b.release()
        #t.sleep(1)

def hilo2():
    global b, c
    while True:
        b.acquire()
        print(f'L')
        c.release()
        #t.sleep(1)

def hilo3():
    global c
    while True:
        c.acquire()
        c.acquire()
        print(f'O') 
        a.release()
        #t.sleep(1)


if __name__ == "__main__":
    th = Thread(target=hilo1)
    th.start()

    th2 = Thread(target=hilo2)
    th2.start()

    th3 = Thread(target=hilo3)
    th3.start()

    th.join()
    th2.join()
    th3.join()

