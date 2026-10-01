import numpy as np
import matplotlib.pyplot as plt
from ej_5 import * 

if __name__ == '__main__':
    def f(x):
        return 1/(1 + x**2)
    
    a, b = -5, 5 # Intervalo
    n = 16  # 17 nodos

    x, y, M = dibujar_spline_cubico(f, a, b, n)


"""

En la práctica anterior, estaba utilizando el polinomio de Newton y, al aumentar el grado,
se producen oscilaciones intensas cerca de (\pm5) (lo que se conoce como fenómeno de Runge). 
En esta práctica, el spline cúbico natural interpola por segmentos y es mucho más estable, 
de modo que se asemeja bastante a (f(x)=\frac{1}{1+x^2}). Por este motivo, las dos curvas son prácticamente idénticas en la gráfica. 
Si calculas (\max|f-S|), el resultado es mucho más pequeño que si se hace con el polinomio de grado 16. # type: ignore

"""