import numpy as np
import matplotlib.pyplot as plt



def euler(f, a, b, n, alfa):
    h = (b - a) / n
    x = np.linspace(a, b, n + 1)
    y = np.zeros(n + 1)
    
    y[0] = alfa
    
    for i in range(n):
        y[i+1] = y[i] + h * f(x[i], y[i])
    
    return x, y


def f(t, p): # Esta funcion se saca igualando D y S
    return 30 - 2*p

for n in [4, 40, 100, 400]:
    t, p = euler(f, 0, 4, n, 20)
    plt.plot(t, p)

plt.show()


"""
Viendo las gráficas, parece que sí hay estabilidad en los precios, porque cuando cogemos valores de n
más grandes, el precio se va acercando cada vez más a un mismo valor. Ese valor es el de equilibrio, que
podemos sacar poniendo p'(t) = 0, entonces queda p = 15. Esto sucede porque al igualar D y S, te queda una
ecuación que es p'(t) = 30 - 2*p(t).
"""