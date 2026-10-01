import numpy as np
import matplotlib.pyplot as plt

def Runge4(f, a, b, n, alpha):
    h = (b - a) / n
    x = np.linspace(a, b, n + 1)
    y = np.zeros(n + 1)

    y[0] = alpha

    for k in range(n):
        K1 = f(x[k], y[k])
        K2 = f(x[k] + h/2, y[k] + h*K1/2)
        K3 = f(x[k] + h/2, y[k] + h*K2/2)
        K4 = f(x[k] + h, y[k] + h*K3)

        y[k+1] = y[k] + h*(K1 + 2*K2 + 2*K3 + K4)/6

    return x, y

def f(t, p):
    return 30 - 2*p


for n in [4, 40, 100, 400]:
    t, p = Runge4(f, 0, 4, n, 20)
    plt.plot(t,p)

plt.show()

"""
Las 3 gráficas de n = 40, n = 100 y n = 400 hacen muy buenas aproximaciones por lo que se solapan. En cambio, la de n = 4
difiere más ya que no tienes suficientes puntos como para hacer una buena aproximación.
"""