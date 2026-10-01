import numpy as np
import matplotlib.pyplot as plt

def f(x):
    return 1/(1+x**2)   # cambia la función

def lagrange(x, y, z):
    n = len(x)
    p = 0.0

    for i in range(n):
        Li = 1.0
        for j in range(n):
            if j != i:
                Li *= (z - x[j]) / (x[i] - x[j])
        p += y[i] * Li

    return p


a = -5
b = 5
N = 11

# nodos
x = np.linspace(a, b, N)
y = f(x)

# puntos finos para evaluar
zz = np.linspace(a, b, 1000)

# interpolador en muchos puntos
pp = np.array([lagrange(x, y, z) for z in zz])

# función real
ff = f(zz)

# error máximo
error_max = np.max(np.abs(ff - pp))
print("Error máximo:", error_max)

# gráfica
plt.plot(zz, ff, label="f(x)")
plt.plot(zz, pp, label="Interpolador Lagrange")
plt.plot(x, y, "o", label="Nodos")
plt.grid()
plt.legend()
plt.show()




#buscar error

a = -2
b = 2
tol = 1e-4

zz = np.linspace(a, b, 2000)
ff = f(zz)

N = 2
error = 1.0

while error > tol:
    N += 1

    x = np.linspace(a, b, N)
    y = f(x)

    pp = np.array([lagrange(x, y, z) for z in zz])

    error = np.max(np.abs(ff - pp))

print("N mínimo:", N)
print("Error:", error)