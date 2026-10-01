import numpy as np
from ej_4 import *
import matplotlib.pyplot as plt

def dibujar_spline_cubico(f, a, b, n):

    # Nodos y datos
    x = np.linspace(a, b, n + 1)
    y = f(x)

    # Spline cúbico natural (función S y momentos M)
    S, M = spline_cubico_natural(x, y)

    # Malla para representar
    xx = np.linspace(a, b, 800)
    yy = f(xx)
    ss = S(xx)

    # Gráfica
    plt.figure()
    plt.plot(xx, yy)
    plt.plot(xx, ss, color='hotpink', alpha = 1)
    plt.plot(x, y, 'o', color ='deeppink')
    plt.grid(True)
    plt.legend()
    plt.title(f'Spline cúbico natural con {n+1} nodos')
    plt.show()

    return x, y, M


if __name__ == '__main__':
    def f(x):
        return np.sin(x) # Cambiar depende la función que te pidan

    a, b = -5, 5 # Intervalo
    n = 16 # Número de nodos -1

    x, y, M = dibujar_spline_cubico(f, a, b, n)
 