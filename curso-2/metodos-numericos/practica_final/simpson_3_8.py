import numpy as np

def f(x):
    return ...

def simpson38(f, a, b, n):
    if n % 3 != 0:
        print("n tiene que ser multiplo de 3")
        return None

    x = np.linspace(a, b, n+1)
    y = f(x)
    h = (b-a)/n

    suma = y[0] + y[n]

    for i in range(1, n):
        if i % 3 == 0:
            suma = suma + 2*y[i]
        else:
            suma = suma + 3*y[i]

    S = 3*h/8 * suma

    return S

