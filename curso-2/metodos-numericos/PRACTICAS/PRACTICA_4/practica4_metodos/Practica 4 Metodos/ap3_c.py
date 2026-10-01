import numpy as np


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

