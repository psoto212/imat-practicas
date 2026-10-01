import numpy as np
import matplotlib.pyplot as plt

def f(x):
    return np.exp(-x**2)

def diferencias_divididas(x, y):
    n = len(x)
    coef = y.astype(float).copy()

    for j in range(1, n):
        for i in range(n-1, j-1, -1):
            coef[i] = (coef[i] - coef[i-1]) / (x[i] - x[i-j])

    return coef


def newton_eval(x, coef, z):
    n = len(coef)
    p = coef[-1]

    for k in range(n-2, -1, -1):
        p = p * (z - x[k]) + coef[k]

    return p


a = -2
b = 2
N = 9

x = np.linspace(a, b, N)
y = f(x)

coef = diferencias_divididas(x, y)

zz = np.linspace(a, b, 1000)

pp = np.array([newton_eval(x, coef, z) for z in zz])
ff = f(zz)

error_max = np.max(np.abs(ff - pp))
print("Error máximo:", error_max)

plt.plot(zz, ff, label="f(x)")
plt.plot(zz, pp, label="Newton")
plt.plot(x, y, "o", label="Nodos")
plt.grid()
plt.legend()
plt.show()

