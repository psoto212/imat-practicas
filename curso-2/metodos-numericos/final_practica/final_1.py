import numpy as np
import matplotlib.pyplot as plt


def regtrap(x, y):
    S = (x[1]- x[0]) * y[0]
    S += np.sum((x[2:]-x[:-2]) * y[1:-1])
    S += (x[-1] -x[-2]) * y[-1]
    return 0.5*S


def f(x):
    return 1/(1+x)

tol = 1e-8
encontrado = False
for k in range(1000):
    exacta = f(k)
    x = np.linspace(0,1, 1000)
    y = np.array(f(x))
    aprox = regtrap(x,y)
    error = abs(exacta - aprox)
    if error < tol and encontrado == False:
        print("iteraciones", k)
        encontrado = True

