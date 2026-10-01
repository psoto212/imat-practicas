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

def p_exacta(t):
    return 15 + 5*np.exp(-2*t)

for n in [4, 40, 100, 400]:
    t, p_r = Runge4(f, 0, 4, n, 20)
    error = np.abs(p_exacta(t) - p_r)
    plt.plot(t, error)

plt.show()


"""
Al estudiar el error cometido, se observa que el método de Runge-Kutta da resultados mucho más precisos que el método de Euler, de hecho, 
el error cometido por Runge-Kutta cuando n no es 4, es practicamente 0. Para los mismos valores de n, el error de Runge-Kutta es bastante 
menor, y esto se ve sobre todo cuando n es pequeño. En cambio, Euler necesita tomar muchos más puntos para aproximarse bien a la solución 
exacta. Por tanto, ambos métodos mejoran al aumentar n, pero Runge-Kutta converge mucho más rápido y aproxima mejor la solución.
"""