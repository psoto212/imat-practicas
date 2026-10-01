import numpy as np
import matplotlib.pyplot as plt


def regtrap(x, y):
    S = (x[1]- x[0]) * y[0]
    S += np.sum((x[2:]-x[:-2]) * y[1:-1])
    S += (x[-1] -x[-2]) * y[-1]
    return 0.5*S


def f(x):
    return np.sqrt(9-x**2)

def g(x):
    return np.pi - f(x)

encontrado = False

for k in range(1000):
    exacta = g(k)
    x = np.linspace(0,3,10000)
    y = np.array(g(x))

    aprox = regtrap(x,y)

    error = abs(exacta - aprox)

    if 1e-6 < error < 1e-5 and encontrado == False:
        encontrado = True
        print(error, "es el error cometido")
        print(aprox, "es la aproximacion")
        print(exacta, "es la exacta")
        print(k, "es le numero de iteraciones")

