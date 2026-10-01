from threading import Thread
import os, time, random

lista = []
suma = 0
def hilo_1():
    global lista
    for i in range(5):
        lista.append(random.randint(1,1000))


def hilo_2():
    global lista, suma
    for i in lista:
        suma += i


if __name__ == "__main__":
    p1 = Thread(target= hilo_1)
    p2 = Thread(target= hilo_2)

    p1.start()
    p1.join()
    p2.start()
    p2.join()
    print(f"la lista es {lista} y la suma de sus valores es {suma}")