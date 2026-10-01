from multiprocessing import Process
import os
import time


def tataranieto():
    print(f"soy el proceso {os.getpid()}, y mi padre es {os.getppid()}")


def bisnieto_1_1():
    print(f"soy el proceso {os.getpid()}, y mi padre es {os.getppid()}")


def bisnieto_1_2():
    print(f"soy el proceso {os.getpid()}, y mi padre es {os.getppid()}")

    p = Process(target = tataranieto)
    p.start()
    p.join()

def bisnieto_2():
    print(f"soy el proceso {os.getpid()}, y mi padre es {os.getppid()}")


def nieto_2():
    print(f"soy el proceso {os.getpid()}, y mi padre es {os.getppid()}")

    procesos = []
    for p in range(3):
        p = Process(target = bisnieto_2)
        procesos.append(p)

    for p in procesos:
        p.start()
    for p in procesos:
        p.join()


def bisnieto_3():
    print(f"soy el proceso {os.getpid()}, y mi padre es {os.getppid()}")


def nieto_3():
    print(f"soy el proceso {os.getpid()}, y mi padre es el proceso {os.getppid()}")

    p = Process(target = bisnieto_3)
    p.start()
    p.join()


def nieto_1_1():
    print(f"soy el proceso {os.getpid()}, y mi padre es el proceso {os.getppid()}")

    p1 = Process(target=bisnieto_1_1)
    p2 = Process(target=bisnieto_1_2)
    p1.start()
    p2.start()
    p1.join()
    p2.join()

def nieto_1_2():
    print(f"sot el proceso {os.getpid()}, y mi padre es {os.getppid()}")



def hijo_1():
    print(f"soy el proceso {os.getpid()}, y mi padre es {os.getppid()}")


    p1 = Process(target = nieto_1_1)
    p1.start()
    p2 = Process(target=nieto_1_2)
    p2.start()

    p1.join()
    p2.join()

def hijo_2():
    print(f"soy el proceso {os.getpid()}, y mi padre es {os.getppid()}")

    p = Process(target = nieto_2)
    p.start()
    p.join()


def hijo_3():
    print(f"soy el proceso {os.getpid()}, y mi padre es {os.getppid()}")
    procesos = []
    for p in range(3):
        p = Process(target=nieto_3)

        procesos.append(p)

    for p in procesos:
        p.start()

    for p in procesos:
        p.join()

        

def hijo_4():
    print(f"soy el proceso {os.getpid()}, y mi padre es {os.getppid()}")

def main():
    print(f"soy el padre {os.getpid}")

    p1 = Process(target=hijo_1)
    p1.start()
    p2 = Process(target=hijo_2)
    p2.start()
    p3 = Process(target=hijo_3)
    p3.start()
    p4 = Process(target = hijo_4)
    p4.start()

    p1.join()
    p2.join()
    p3.join()
    p4.join()





if __name__ == "__main__":
    main()

