import numpy as np

def euler(f, a, b, n, alfa):
    h = (b - a) / n
    x = np.linspace(a, b, n + 1)
    y = np.zeros(n + 1)
    
    y[0] = alfa
    
    for i in range(n):
        y[i+1] = y[i] + h * f(x[i], y[i])
    
    return x, y


