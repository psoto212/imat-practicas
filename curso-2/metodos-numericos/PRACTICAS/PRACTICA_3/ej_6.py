import numpy as np
import matplotlib.pyplot as plt
from ej_4 import spline_cubico_natural  # donde tengas el ejercicio 4

def dibujar_spline_cubico_natural(f, a, b, n, num_plot=1000):
    """
    Dibuja f y su spline cúbico natural interpolador usando n+1 nodos equiespaciados en [a,b].
    """
    # Nodos y datos
    x = np.linspace(a, b, n + 1)
    y = f(x)

    # Spline cúbico natural (función S y momentos M)
    S, M = spline_cubico_natural(x, y)

    # Malla fina para representar
    xx = np.linspace(a, b, num_plot)
    yy = f(xx)
    ss = S(xx)

    # Gráfica
    plt.figure(figsize=(9, 5))
    plt.plot(xx, yy, label='f(x)')
    plt.plot(xx, ss, label='Spline cúbico natural')
    plt.plot(x, y, 'o', label='Nodos')
    plt.grid(True, alpha=0.3)
    plt.title(f'Spline cúbico natural con {n+1} nodos en [{a},{b}]')
    plt.legend()
    plt.show()

    return x, y, M

if __name__ == '__main__':
    # Ejemplo de uso (puedes cambiar f, intervalo y n)
    def f(x):
        return 1/(1 + x**2)

    a, b = -5, 5
    n = 16  # 17 nodos

    x, y, M = dibujar_spline_cubico_natural(f, a, b, n)





"""

En la práctica anterior, estaba utilizando el polinomio de Newton y, al aumentar el grado,
se producen oscilaciones intensas cerca de (\pm5) (lo que se conoce como fenómeno de Runge). 
En esta práctica, el spline cúbico natural interpola por segmentos y es mucho más estable, 
de modo que se asemeja bastante a (f(x)=\frac{1}{1+x^2}). Por este motivo, las dos curvas son prácticamente idénticas en la gráfica. 
Si calculas (\max|f-S|), el resultado es mucho más pequeño que si se hace con el polinomio de grado 16. # type: ignore

"""