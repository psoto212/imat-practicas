
from multiprocessing import Process
import time
import math


def aproximar_pi(limite):
    """Función que aproxima el número pi usando la serie infinita."""
    suma = 0
    for n in range(1, limite + 1):
        suma += 1 / (n ** 2)
    pi = math.sqrt(6 * suma)
    return pi


def version_un_proceso():
    """Ejecuta la función de forma secuencial (un solo proceso)."""
    valores = [1_000_000, 2_000_000, 4_000_000, 8_000_000]
    tiempos = []

    print("Versión con un solo proceso:\n")

    for limite in valores:
        inicio = time.time()
        resultado = aproximar_pi(limite)
        fin = time.time()
        duracion = fin - inicio
        tiempos.append(duracion)

        print(f"Con un valor de {limite:,}, el resultado es {resultado:.8f}, con un tiempo de {duracion:.4f} segundos")

    return sum(tiempos)  # tiempo total para comparar el speedUp


def calcular_pi_en_proceso(limite):
    """Función que ejecuta cada proceso de la versión multiproceso."""
    inicio = time.time()
    resultado = aproximar_pi(limite)
    fin = time.time()
    print(f"Con un valor de {limite:,}, el resultado es {resultado:.8f}, con un tiempo de {fin - inicio:.4f} segundos")


def version_multiproceso():
    """Ejecuta la función usando 4 procesos en paralelo."""
    valores = [1_000_000, 2_000_000, 4_000_000, 8_000_000]
    procesos = []
    inicio_total = time.time()

    print("Versión con múltiples procesos:\n")

    # Crear y arrancar cada proceso
    for limite in valores:
        proceso = Process(target=calcular_pi_en_proceso, args=(limite,))
        procesos.append(proceso)
        proceso.start()

    # Esperar a que todos terminen
    for proceso in procesos:
        proceso.join()

    fin_total = time.time()
    duracion_total = fin_total - inicio_total
    print(f"\nTiempo total (versión multiproceso): {duracion_total:.4f} segundos")
    return duracion_total


if __name__ == "__main__":
    print("=== Ejercicio 4: Pequeño Benchmark ===\n")
    print("1. Versión con un proceso")
    print("2. Versión con múltiples procesos")

    opcion = int(input("\nElige una opción (1 o 2): "))

    if opcion == 1:
        tiempo_un_proceso = version_un_proceso()
        print(f"\nTiempo total (versión un proceso): {tiempo_un_proceso:.4f} segundos")

    elif opcion == 2:
        tiempo_multiproceso = version_multiproceso()
        print(f"\nVersión multiproceso ejecutada correctamente.")
    else:
        print("Opción no válida. Fin del programa.")

