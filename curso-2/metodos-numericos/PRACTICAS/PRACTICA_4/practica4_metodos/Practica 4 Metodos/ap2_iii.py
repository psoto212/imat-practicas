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

def f(t, p):
    return 30 - 2*p

def p_exacta(t): # Solución calculada a mano
    return 15 + 5*np.exp(-2*t)

for n in [4, 40, 100, 400]:
    t, p_euler = euler(f, 0, 4, n, 20)
    error = np.abs(p_exacta(t) - p_euler)
    plt.plot(t, error)
plt.show()

"""
En la gráfica se ve que para n = 4 el error es bastante grande, así que en ese caso el método de Euler 
no aproxima bien la solución exacta. Esto pasa porque el paso es demasiado grande y por eso la aproximación oscila mucho.
En cambio, para n=40, n=100 y n=400, el error es mucho más pequeño y además va disminuyendo según aumentamos
n. Es decir, cuanto más puntos cogemos en la partición, mejor se aproxima el método de Euler a la solución exacta.
Por tanto, los resultados son los esperados, tomando más puntos la aproximación mejora claramente y el error 
tiende a hacerse cada vez menor.
"""