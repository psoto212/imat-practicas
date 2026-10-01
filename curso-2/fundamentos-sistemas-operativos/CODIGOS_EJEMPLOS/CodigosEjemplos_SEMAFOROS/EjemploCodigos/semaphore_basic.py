from multiprocessing.pool import ThreadPool

# Sin semaforos
valor = 0
def funcion(iteracion: int):
    global valor
    for i in range(iteracion):
        c = valor
        valor = c + 1

if __name__ == '__main__':
    pool = ThreadPool(2)
    pool.map(funcion, [20000000, 20000000])
    pool.close()
    pool.join()

    print(f"Valor es {valor}")
