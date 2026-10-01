from threading import Thread, Semaphore
import time
import random
import os
import random


N = 4
plazas = Semaphore(0)        # el entrenador deja pasar a 4 al grupo
grupo_lleno = Semaphore(0)  # el 4º avisa al entrenador
fin = Semaphore(0)          # entrenador libera a los 4

mutex = Semaphore(1)
cont = 0

def jugador(i):
    global cont
    plazas.acquire()              # espera a que el entrenador forme grupo

    mutex.acquire()
    cont += 1
    if cont == N:
        grupo_lleno.release()     # el 4º avisa
        cont = 0
    mutex.release()

    fin.acquire()                 # espera la orden del entrenador
    # empieza_ejercicio()

def entrenador():
    while True:
        plazas.release(N)         # forma grupo de 4
        grupo_lleno.acquire()     # espera a que estén los 4
        # dar_orden()
        fin.release(N)            # deja continuar a los 4

        grupo.acquire()
        aforo.release(4)


