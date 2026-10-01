import numpy as np

def f(x):
    return np.exp(-x)

def punto_medio(f, a, b, n):
    h = (b-a)/n
    suma = 0

    for i in range(n):
        xi = a + i*h
        medio = xi + h/2
        suma = suma + f(medio)

    S = h*suma
    return S

s = punto_medio(f, 0, 2, 4)
print(s)