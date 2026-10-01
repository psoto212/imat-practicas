import numpy as np

def f(x):
    return np.exp(-x)

def rectangulo_der(f, a, b, n):
    h = (b-a)/n
    suma = 0

    for i in range(1, n+1):
        x = a + i*h
        suma = suma + f(x)

    S = h*suma
    return S

s = rectangulo_der(f, 0, 2, 4)
print(s)