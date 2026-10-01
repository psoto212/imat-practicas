import numpy as np
import matplotlib.pyplot as plt

def f(x):
    return np.exp(-x**2)

def spline_lineal(x, y, z):
    n = len(x)

    for i in range(n-1):
        if x[i] <= z <= x[i+1]:
            return y[i] + (y[i+1]-y[i])/(x[i+1]-x[i])*(z-x[i])

    raise ValueError("z fuera del intervalo")


a = -2
b = 2
N = 9

x = np.linspace(a, b, N)
y = f(x)

zz = np.linspace(a, b, 1000)

ss = np.array([spline_lineal(x, y, z) for z in zz])
ff = f(zz)

error_max = np.max(np.abs(ff - ss))
print("Error máximo:", error_max)

plt.plot(zz, ff, label="f(x)")
plt.plot(zz, ss, label="Spline lineal")
plt.plot(x, y, "o", label="Nodos")
plt.grid()
plt.legend()
plt.show()