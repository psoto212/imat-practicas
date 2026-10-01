import numpy as np

def f(x):
    return np.exp(-x)

def simpson13(f, a, b, n):
    if n % 2 != 0:
        print("n tiene que ser par")
        return None

    x = np.linspace(a, b, n+1)
    y = f(x)
    h = (b-a)/n

    suma = y[0] + y[n]

    for i in range(1, n):
        if i % 2 == 1:
            suma = suma + 4*y[i]
        else:
            suma = suma + 2*y[i]

    S = h/3 * suma

    return S

s = simpson13(f, 0, 2, 4)
print(s)
